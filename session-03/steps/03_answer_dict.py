"""
3단계 — 답변 목록을 딕셔너리로 모으기 (슬라이드 16~18쪽)
답변을 추가할 때 answers에 한 줄만 추가하면 됩니다.

실행: python -m chainlit run steps/03_answer_dict.py -w
"""
import chainlit as cl

answers = {
    "공부": "오늘 할 일을 작게 나눠보세요.",
    "진로": "좋아하는 과목부터 적어보세요.",
    "친구": "상대 이야기를 먼저 들어보세요.",
    "급식": "오늘 메뉴를 확인해보면 좋겠어요.",
    "운동": "가볍게 10분부터 시작해보세요.",
}


def answer(user_text):
    for keyword, reply in answers.items():
        if keyword in user_text:
            return reply
    return "조금 더 자세히 말해줄래요?"


@cl.on_message
async def on_message(message: cl.Message):
    reply = answer(message.content)
    await cl.Message(content=reply).send()
