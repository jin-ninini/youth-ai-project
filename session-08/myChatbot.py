# 터미널에서 chainlit 설치
# python -m pip install chainlit

import chainlit as cl

# 챗봇 클래스 정의
class AdviceBot:
    def __init__(self, name):
        self.name = name
        self.answers = {
            "공부": "오늘 할 일을 작게 나눠보세요.",
            "진로": "좋아하는 과목부터 적어보세요.",
            "친구": "상대 이야기를 먼저 들어보세요."
            }
    
    # 모드 설정
    def find_mode(self, user_text):
        if "짧게" in user_text:
            return "short"
        elif "자세히" in user_text:
            return "detail"
        else:
            return "normal"

    # 모드에 따라 답변 생성
    def answer(self, user_text):
        mode = self.find_mode(user_text)
        for keyword, reply in self.answers.items():
            if keyword in user_text:
                if mode == "detail":
                    return f"{self.name}: {reply} 작은 예시부터 시작해보세요."
                return f"{self.name}: {reply}"
        return f"{self.name}: 조금 더 자세히 말해줄래요?"

# 챗봇 객체 생성   
bot = AdviceBot("학교생활봇")

# Chainlit 연결
@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("count", 0)
    await cl.Message(content="안녕하세요. 질문을 입력해보세요.").send()

@cl.on_message
async def on_message(message: cl.Message):
    count = cl.user_session.get("count") + 1
    cl.user_session.set("count", count)
    reply = bot.answer(message.content)
    await cl.Message(content=f"{count}번째 질문입니다) {reply}").send()

# 터미널에서 Chainlit 실행
# python -m chainlit run myChatbot.py -w
# 실행 후 8000번 포트 확인