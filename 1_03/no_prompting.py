import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import OpenAI
from config.const import OPENAI_API_KEY
from config.log_config import logger


client = OpenAI(api_key= OPENAI_API_KEY)

response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.9,
    messages = [
        {
            "role" : "system",
            "content" : "너는 유치원생이야. 유치원생처럼 답변해 줘."
        },
        {
            "role" : "user",
            "content" : "참새"
        },
        {
            "role" : "assistant",
            "content" : "짹짹"
        },
        {
            "role" : "user",
            "content" : "오리"
        },
                {
            "role" : "assistant",
            "content" : "꽥꽥"
        },
        {
            "role" : "user",
            "content" : "개구리"
        },
                {
            "role" : "assistant",
            "content" : "개굴개굴"
        },
        {
            "role" : "user",
            "content" : "병아리"
        }
    ]
)

logger.info(response)
logger.info("-----------------")
logger.info(response.choices[0].message.content)