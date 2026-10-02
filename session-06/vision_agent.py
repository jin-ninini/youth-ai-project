"""
🖼️ 이미지를 보는 에이전트 — Agent-Framework-Samples 04.Tools (vision) 실습
https://github.com/microsoft/Agent-Framework-Samples/tree/main/04.Tools

원본은 Azure AI Foundry 클라이언트로 가구 사진을 분석하지만,
여기서는 APIM의 VISION_MODEL로 연결해 수업 중 만든 그래프 이미지를 설명합니다.

실행 (session-06 폴더에서): python vision_agent.py [이미지경로] ["질문"]
기본 이미지: data/graph.png (01_function_calling_agent.ipynb 수학 에이전트가 그린 그래프)
"""
import asyncio
import base64
import mimetypes
import os
import sys
from pathlib import Path

from agent_framework import Agent, Content, Message

from src.llm_client import build_chat_client, check_env

DEFAULT_IMAGE = Path(__file__).parent / "data" / "graph.png"


def image_to_content(path: Path) -> Content:
    """이미지 파일을 모델에 보낼 수 있는 data URI 콘텐츠로 바꾼다."""
    media_type = mimetypes.guess_type(path.name)[0] or "image/png"
    encoded = base64.b64encode(path.read_bytes()).decode()
    return Content.from_uri(uri=f"data:{media_type};base64,{encoded}", media_type=media_type)


async def main():
    if not check_env():
        return

    image_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_IMAGE
    question = sys.argv[2] if len(sys.argv) > 2 else "이 이미지가 무엇을 보여주는지 고등학생에게 설명해줘."

    agent = Agent(
        client=build_chat_client(os.getenv("VISION_MODEL")),
        name="비전도우미",
        instructions="너는 이미지를 꼼꼼히 관찰하고 핵심을 3~4문장으로 설명하는 선생님이야. 한국어로 답해.",
    )

    print(f"🖼️ 이미지: {image_path}\n🙋 질문: {question}\n")
    message = Message("user", [Content.from_text(text=question), image_to_content(image_path)])
    response = await agent.run(message)
    print(f"🤖 {response.text}")


if __name__ == "__main__":
    asyncio.run(main())
