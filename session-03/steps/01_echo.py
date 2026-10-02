"""
1단계 — Chainlit 화면에 연결하기 (슬라이드 8~10쪽)
채팅창에 입력한 문장을 그대로 다시 보여줍니다.

실행: python -m chainlit run steps/01_echo.py -w
"""
import chainlit as cl


@cl.on_message
async def on_message(message: cl.Message):
    user_text = message.content
    await cl.Message(content=f"[1팀 챗봇] 입력한 내용: {user_text}").send()
