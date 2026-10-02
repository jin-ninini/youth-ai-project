"""
5단계 — 다음 시간 맛보기: 문장이 숫자로 바뀌는 흐름 (슬라이드 46~48쪽)
실제 LLM은 아니고, '토큰화 → 숫자 변환' 흐름만 흉내 냅니다.

실행: python -m chainlit run steps/05_llm_preview.py -w
"""
import chainlit as cl


class TextProcessPreview:
    def tokenize(self, text):
        return text.split()

    def to_numbers(self, tokens):
        return [len(token) for token in tokens]

    def make_preview(self, text):
        tokens = self.tokenize(text)
        numbers = self.to_numbers(tokens)
        return f"""입력 문장:
{text}

1단계. 문장을 작은 조각으로 나누기:
{tokens}

2단계. 각 조각을 간단한 숫자로 바꿔보기:
{numbers}
"""


preview = TextProcessPreview()


@cl.on_message
async def on_message(message: cl.Message):
    result = preview.make_preview(message.content)
    await cl.Message(content=result).send()
