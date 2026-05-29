"""
Microsoft Agent Framework 실습 - 고등학생을 위한 샘플 시나리오
====================================================================

이 파일은 .ipynb 노트북과 같은 내용을 일반 Python 스크립트로 만든 거예요.
주피터 노트북이 없는 환경에서도 그대로 실행할 수 있습니다.

실행 방법:
    pip install agent-framework
    cp setup-apim/.env.sample ../.env
    # ../.env에 APIM_BASE_URL, APIM_KEY, CHAT_MODEL 값을 채운 뒤
    python maf_sample_scenarios.py
"""

import asyncio
import os
from pathlib import Path
from typing import Annotated

from dotenv import load_dotenv
from pydantic import Field

from agent_framework import Agent, WorkflowBuilder, AgentExecutor
from agent_framework.openai import OpenAIChatClient


ENV_PATH = (Path(__file__).resolve().parent / "../.env").resolve()
load_dotenv(ENV_PATH, override=True)


def build_chat_client() -> OpenAIChatClient:
    apim_base_url = os.environ["APIM_BASE_URL"].rstrip("/")
    apim_key = os.environ["APIM_KEY"]
    model = os.getenv("CHAT_MODEL", "gpt-5.4")
    return OpenAIChatClient(
        model=model,
        base_url=f"{apim_base_url}/{model}/",
        api_key="placeholder",
        default_headers={"api-key": apim_key},
    )


# ====================================================================
# 시나리오 1. Hello, Agent!
# ====================================================================
async def scenario_1_hello():
    print("\n" + "=" * 60)
    print("📌 시나리오 1. Hello, Agent!")
    print("=" * 60)

    greeter = Agent(
        client=build_chat_client(),
        name="인사봇",
        instructions=(
            "너는 친절한 인사 도우미야. "
            "항상 밝고 따뜻하게, 한국어로 대답해. "
            "이모지를 적절히 사용해도 좋아."
        ),
    )

    response = await greeter.run("안녕! 너는 누구니?")
    print("\n[에이전트의 답변]")
    print(response.text)


# ====================================================================
# 시나리오 2. 도구를 쓰는 에이전트
# ====================================================================
def add(
    a: Annotated[float, Field(description="첫 번째 숫자")],
    b: Annotated[float, Field(description="두 번째 숫자")],
) -> float:
    """두 숫자를 더한 값을 돌려준다."""
    return a + b


def multiply(
    a: Annotated[float, Field(description="첫 번째 숫자")],
    b: Annotated[float, Field(description="두 번째 숫자")],
) -> float:
    """두 숫자를 곱한 값을 돌려준다."""
    return a * b


def power(
    base: Annotated[float, Field(description="밑")],
    exp: Annotated[float, Field(description="지수")],
) -> float:
    """base의 exp 제곱을 돌려준다."""
    return base ** exp


async def scenario_2_tools():
    print("\n" + "=" * 60)
    print("📌 시나리오 2. 도구를 쓰는 에이전트")
    print("=" * 60)

    math_helper = Agent(
        client=build_chat_client(),
        name="수학도우미",
        instructions=(
            "너는 수학 문제를 도와주는 친절한 튜터야. "
            "계산이 필요하면 반드시 제공된 도구(add, multiply, power)를 사용해서 답을 구해. "
            "머릿속으로 계산하지 말고 도구를 호출해야 정확해."
        ),
        tools=[add, multiply, power],
    )

    response = await math_helper.run("235 × 47은 얼마야? 그리고 그 결과를 제곱하면?")
    print("\n[에이전트의 답변]")
    print(response.text)


# ====================================================================
# 시나리오 3. 두 에이전트의 협업 (작가 + 편집자)
# ====================================================================
async def scenario_3_collaboration():
    print("\n" + "=" * 60)
    print("📌 시나리오 3. 두 에이전트의 협업")
    print("=" * 60)

    writer = Agent(
        client=build_chat_client(),
        name="작가",
        instructions=(
            "너는 감성적인 단편 작가야. "
            "주제를 받으면 한국어로 4~5문장의 짧은 글을 써. "
            "비유와 묘사를 풍부하게 사용해."
        ),
    )

    editor = Agent(
        client=build_chat_client(),
        name="편집자",
        instructions=(
            "너는 꼼꼼한 편집자야. "
            "받은 글을 읽고, 더 좋아질 수 있는 부분 2~3가지를 짚어줘. "
            "건설적이고 친절한 어조로 피드백해."
        ),
    )

    topic = "비 오는 날의 등굣길"
    draft = await writer.run(f"주제: {topic}. 이 주제로 짧은 글을 써줘.")
    print("\n📝 [작가의 초안]")
    print(draft.text)

    feedback = await editor.run(
        f"아래는 작가가 쓴 글이야. 어떻게 더 좋아질 수 있을지 의견을 줘.\n\n{draft.text}"
    )
    print("\n🧐 [편집자의 피드백]")
    print(feedback.text)

    final = await writer.run(
        f"네가 쓴 글에 대한 편집자의 피드백이야:\n{feedback.text}\n\n"
        f"이 피드백을 반영해서 글을 다시 써줘."
    )
    print("\n✨ [작가의 최종본]")
    print(final.text)


# ====================================================================
# 시나리오 4. 워크플로우 (요약 → 번역 자동 파이프라인)
# ====================================================================
async def scenario_4_workflow():
    print("\n" + "=" * 60)
    print("📌 시나리오 4. 워크플로우 만들기")
    print("=" * 60)

    summarizer = Agent(
        client=build_chat_client(),
        name="요약가",
        instructions="긴 문장을 한 줄로 핵심만 요약해. 한국어로.",
    )

    translator = Agent(
        client=build_chat_client(),
        name="번역가",
        instructions="입력 받은 한국어 문장을 자연스러운 영어로 번역해.",
    )

    summarize_step = AgentExecutor(summarizer, id="summarize")
    translate_step = AgentExecutor(translator, id="translate")

    workflow = (
        WorkflowBuilder()
        .set_start_executor(summarize_step)
        .add_edge(summarize_step, translate_step)
        .build()
    )

    long_text = (
        "오늘 학교에서 과학 수업 시간에 인공지능에 대해 배웠다. "
        "선생님께서는 AI가 단순히 챗봇이 아니라 스스로 도구를 사용하고 "
        "여러 단계를 거쳐 일을 해내는 에이전트로 발전하고 있다고 하셨다. "
        "수업이 끝나고 친구들과 함께 다음 주에 직접 만들어 보기로 했다."
    )

    print("\n📥 [입력]")
    print(long_text)

    events = await workflow.run(long_text)

    print("\n📤 [최종 결과]")
    print(events.get_outputs())


# ====================================================================
# 메인
# ====================================================================
async def main():
    if not os.environ.get("APIM_BASE_URL") or not os.environ.get("APIM_KEY"):
        print("⚠️  APIM 환경 변수를 먼저 설정해 주세요.")
        print("   1) cp setup-apim/.env.sample ../.env")
        print("   2) ../.env에 APIM_BASE_URL, APIM_KEY를 입력하세요.")
        return

    print("🚀 Microsoft Agent Framework 실습을 시작합니다!\n")

    # 원하는 시나리오만 켜고 끄려면 아래에서 주석을 조절하세요.
    await scenario_1_hello()
    await scenario_2_tools()
    await scenario_3_collaboration()
    await scenario_4_workflow()

    print("\n" + "=" * 60)
    print("🎓 수고하셨습니다! 이제 여러분만의 에이전트를 만들어 보세요.")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
