"""
2단계 — 답변 기능을 함수로 분리하기 (슬라이드 12~15쪽)
Chainlit은 화면 처리, answer 함수는 답변 처리를 맡습니다.

실행: python -m chainlit run steps/02_answer_function.py -w
"""
import chainlit as cl


def answer(user_text):
    if "공부" in user_text:
        return "오늘 할 일을 작게 나눠보세요."
    elif "진로" in user_text:
        return "좋아하는 과목부터 적어보세요."
    elif "친구" in user_text:
        return "상대 이야기를 먼저 들어보세요."
    else:
        return "조금 더 자세히 말해줄래요?"


@cl.on_message
async def on_message(message: cl.Message):
    user_text = message.content
    reply = answer(user_text)
    await cl.Message(content=reply).send()
