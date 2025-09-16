# config/const.py
import os
from dotenv import load_dotenv

load_dotenv()

# 환경변수에서 가져오기
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# API 키가 없을 경우 에러 처리
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY 환경변수를 설정해주세요")