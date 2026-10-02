"""
APIM(Foundry Proxy) 연결용 MAF 클라이언트 — 6회차 실행 스크립트들이 공통으로 사용합니다.

엔드포인트 구조: {APIM_BASE_URL}/{MODEL_NAME}/   (인증: "api-key" 헤더)
.env는 프로젝트 루트에 두면 자동으로 찾습니다.
"""
import os

from dotenv import find_dotenv, load_dotenv
from agent_framework.openai import OpenAIChatCompletionClient

load_dotenv(find_dotenv(usecwd=True), override=True)


def check_env() -> bool:
    """APIM 환경 변수가 설정됐는지 확인하고, 없으면 안내 문구를 출력한다."""
    if os.environ.get("APIM_BASE_URL") and os.environ.get("APIM_KEY"):
        return True
    print("⚠️  APIM 환경 변수를 먼저 설정해 주세요.")
    print("   1) 프로젝트 루트에서 cp .env.example .env")
    print("   2) .env에 APIM_BASE_URL, APIM_KEY를 입력하세요.")
    return False


def build_chat_client(model: str | None = None) -> OpenAIChatCompletionClient:
    """채팅 모델용 MAF 클라이언트를 만든다. model을 생략하면 .env의 CHAT_MODEL을 사용한다.

    Chat Completions API는 매 요청에 대화 전체를 보내므로(stateless),
    도구 호출 중 `previous_response_id`를 찾지 못하는 APIM 프록시 환경에서도 안정적으로 동작한다.
    """
    model = model or os.getenv("CHAT_MODEL", "gpt-5.4")
    return OpenAIChatCompletionClient(
        model=model,
        base_url=f"{os.environ['APIM_BASE_URL'].rstrip('/')}/{model}/",
        api_key="placeholder",  # APIM은 api-key 헤더로 인증
        default_headers={"api-key": os.environ["APIM_KEY"]},
    )
