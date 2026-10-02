"""
🚀 보너스 — 규칙 기반 챗봇을 LLM 챗봇으로 바꿔보기 (슬라이드 45~46쪽 "다음 시간으로 이어지는 생각")

myChatbot.py는 answers에 없는 질문에 답하지 못합니다.
이 파일은 같은 Chainlit 화면에 LLM(APIM Foundry Proxy)을 연결해, 규칙 없이 문맥에 맞는 답변을 생성합니다.

준비: 프로젝트 루트의 .env에 APIM_BASE_URL, APIM_KEY, CHAT_MODEL 설정
실행: python -m chainlit run llm_chatbot.py -w
"""
import os

import chainlit as cl
from dotenv import find_dotenv, load_dotenv
from openai import AsyncOpenAI

load_dotenv(find_dotenv(usecwd=True), override=True)

CHAT_MODEL = os.getenv("CHAT_MODEL", "gpt-5.4")
client = AsyncOpenAI(
    base_url=f"{os.environ['APIM_BASE_URL'].rstrip('/')}/{CHAT_MODEL}/",
    api_key="placeholder",  # APIM은 api-key 헤더로 인증
    default_headers={"api-key": os.environ["APIM_KEY"]},
)

SYSTEM_PROMPT = (
    "너는 고등학생의 학교생활을 돕는 '학교생활봇'이야. "
    "공부, 진로, 친구, 급식, 운동 고민에 친절하게 3문장 이내로 답해. "
    "사용자가 '짧게'라고 하면 1문장, '자세히'라고 하면 예시를 포함해 답해."
)


@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("history", [{"role": "system", "content": SYSTEM_PROMPT}])
    await cl.Message(content="안녕하세요. LLM 학교생활봇입니다. 무엇이든 물어보세요.").send()


@cl.on_message
async def on_message(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})
    response = await client.chat.completions.create(
        model=CHAT_MODEL, messages=history, max_completion_tokens=400
    )
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    await cl.Message(content=reply).send()
