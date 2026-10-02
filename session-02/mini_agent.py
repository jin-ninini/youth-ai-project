"""
🤖 미니 에이전트 — 2회차 최종 실습
입력받고 → 규칙 확인하고 → 답하는 프로그램 (슬라이드 36~37쪽 클래스 버전)

실행: python mini_agent.py
종료: '종료' 입력
"""


class StudentAgent:
    def __init__(self, name="고민상담봇"):
        self.name = name
        self.answers = {
            "공부": "오늘 할 일을 10분짜리로 나눠보세요.",
            "진로": "좋아하는 것과 잘하는 것을 같이 적어보세요.",
            "친구": "상대 이야기를 먼저 들어보세요.",
            "저축": "작게라도 목표 금액을 정해보세요.",
        }

    def respond(self, question):
        for keyword, reply in self.answers.items():
            if keyword in question:
                return f"{self.name}: {reply}"
        return f"{self.name}: 조금 더 자세히 말해줄래요?"


def main():
    agent = StudentAgent()
    print(f"안녕하세요, 저는 {agent.name}입니다. (그만하려면 '종료')")
    while True:
        try:
            question = input("고민: ").strip()
        except EOFError:
            break
        if question == "종료":
            break
        print(agent.respond(question))
    print("다음에 또 만나요!")


if __name__ == "__main__":
    main()
