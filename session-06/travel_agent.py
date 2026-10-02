"""
✈️ 나의 첫 여행 에이전트 — Agent-Framework-Samples 02.CreateYourFirstAgent 실습
https://github.com/microsoft/Agent-Framework-Samples/tree/main/02.CreateYourFirstAgent

원본은 GitHub Models를 쓰지만, 여기서는 수업용 APIM(Foundry Proxy)으로 연결합니다.
에이전트는 '랜덤 여행지 뽑기' 도구를 스스로 호출해서 당일치기 여행 계획을 세웁니다.

실행 (session-06 폴더에서): python travel_agent.py ["요청 문장"]
"""
import asyncio
import random
import sys

from agent_framework import Agent

from src.llm_client import build_chat_client, check_env


def get_random_destination() -> str:
    """국내 당일치기 여행지 하나를 무작위로 골라 돌려준다."""
    destinations = [
        "경주", "전주 한옥마을", "강릉", "부산 해운대", "인천 차이나타운",
        "춘천 남이섬", "수원 화성", "여수 밤바다", "단양", "제주 성산일출봉",
    ]
    return random.choice(destinations)


async def main():
    if not check_env():
        return

    agent = Agent(
        client=build_chat_client(),
        name="여행플래너",
        instructions=(
            "너는 고등학생을 위한 여행 플래너야. "
            "여행지가 정해지지 않았으면 반드시 get_random_destination 도구로 여행지를 뽑아. "
            "오전·점심·오후 일정과 예상 비용을 짧게 정리해서 한국어로 답해."
        ),
        tools=[get_random_destination],
    )

    request = " ".join(sys.argv[1:]) or "이번 주말에 친구랑 갈 당일치기 여행 계획 짜줘"
    print(f"🙋 요청: {request}\n")
    response = await agent.run(request)
    print("✈️ AI 여행 계획")
    print("=" * 50)
    print(response.text)
    print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())
