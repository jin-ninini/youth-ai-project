"""
4단계 — 클래스로 정리하기 (슬라이드 20~28쪽)
answers(속성)와 answer(메서드)를 AdviceBot 객체 하나로 묶습니다.

실행: python -m chainlit run steps/04_advice_bot_class.py -w
"""
import chainlit as cl


class AdviceBot:
    def __init__(self, name):
        self.name = name
        self.answers = {
            "공부": "오늘 할 일을 작게 나눠보세요.",
            "진로": "좋아하는 과목부터 적어보세요.",
            "친구": "상대 이야기를 먼저 들어보세요.",
        }

    def answer(self, user_text):
        for keyword, reply in self.answers.items():
            if keyword in user_text:
                return f"{self.name}: {reply}"
        return f"{self.name}: 조금 더 자세히 말해줄래요?"


bot = AdviceBot("2팀 상담봇")


@cl.on_message
async def on_message(message: cl.Message):
    reply = bot.answer(message.content)
    await cl.Message(content=reply).send()
