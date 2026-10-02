"""
🔀 조건 분기 워크플로우 — Agent-Framework-Samples 07.Workflow (condition) 실습
https://github.com/microsoft/Agent-Framework-Samples/tree/main/07.Workflow

원본: 작가(evangelist) → 검토자(reviewer) → 통과하면 발행(publisher), 아니면 반려
여기서는 '학교 신문 기사'로 바꿔서 APIM 모델로 실행하고, 발행은 data/output/에 Markdown 파일로 저장합니다.

    기자 ──▶ 편집장 ──▶ 검토 결과 정리 ──┬─(승인)──▶ 발행 (파일 저장)
                                          └─(반려)──▶ 반려 안내

실행 (session-07 폴더에서): python conditional_workflow.py ["기사 주제" ...]
"""
import asyncio
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Literal

from pydantic import BaseModel

from agent_framework import Agent, AgentExecutor, AgentExecutorResponse, WorkflowBuilder, WorkflowContext, executor

from src.llm_client import build_chat_client, check_env

OUTPUT_DIR = Path(__file__).parent / "data" / "output"


class Review(BaseModel):
    """편집장이 돌려줄 JSON 형식"""
    review_result: Literal["Yes", "No"]
    reason: str
    draft_content: str


@dataclass
class ReviewResult:
    approved: bool
    reason: str
    draft_content: str


@executor(id="to_review_result")
async def to_review_result(response: AgentExecutorResponse, ctx: WorkflowContext[ReviewResult]) -> None:
    """편집장 답변(JSON)을 파이썬 객체로 바꿔 다음 단계로 넘긴다."""
    review = Review.model_validate_json(response.agent_response.text)
    await ctx.send_message(ReviewResult(review.review_result == "Yes", review.reason, review.draft_content))


@executor(id="publish")
async def publish(review: ReviewResult, ctx: WorkflowContext[None, str]) -> None:
    """승인된 기사를 Markdown 파일로 저장한다. (원본의 publisher 에이전트 역할)"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / f"{datetime.now():%Y%m%d%H%M%S}.md"
    path.write_text(review.draft_content, encoding="utf-8")
    await ctx.yield_output(f"✅ 승인 — {review.reason}\n📰 발행 완료: {path}\n\n{review.draft_content}")


@executor(id="reject")
async def reject(review: ReviewResult, ctx: WorkflowContext[None, str]) -> None:
    await ctx.yield_output(f"❌ 반려 — {review.reason}")


def build_workflow():
    client = build_chat_client()
    reporter = AgentExecutor(
        Agent(
            client=client,
            name="학생기자",
            instructions="너는 고등학교 신문의 학생 기자야. 주어진 주제로 제목과 4~6문장 본문의 짧은 기사를 Markdown으로 써.",
        ),
        id="reporter",
    )
    editor = AgentExecutor(
        Agent(
            client=client,
            name="편집장",
            instructions=(
                "너는 고등학교 신문 편집장이야. 기사가 학생 신문에 실리기에 적절한지 검토해.\n"
                "부정행위·위험한 행동을 부추기거나 특정인을 비방하면 review_result를 'No'로, 그 외에는 'Yes'로 해.\n"
                "reason에는 한 문장 이유를, draft_content에는 기사 원문을 그대로 넣어."
            ),
            default_options={"response_format": Review},
        ),
        id="editor",
    )
    return (
        WorkflowBuilder(start_executor=reporter)
        .add_edge(reporter, editor)
        .add_edge(editor, to_review_result)
        .add_edge(to_review_result, publish, condition=lambda r: r.approved)
        .add_edge(to_review_result, reject, condition=lambda r: not r.approved)
        .build()
    )


async def main():
    if not check_env():
        return

    topics = sys.argv[1:] or ["우리 학교 AI 동아리가 해커톤에서 상을 받았다", "시험 문제를 몰래 미리 보는 꿀팁"]
    for topic in topics:
        print("=" * 60)
        print(f"📝 주제: {topic}")
        events = await build_workflow().run(f"기사 주제: {topic}")
        # 기자·편집장 에이전트의 중간 응답도 outputs에 담기므로, 최종 결과(문자열)만 출력
        for output in events.get_outputs():
            if isinstance(output, str):
                print(output)


if __name__ == "__main__":
    asyncio.run(main())
