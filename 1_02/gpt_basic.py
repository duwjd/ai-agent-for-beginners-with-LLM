import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import OpenAI
from config.const import OPENAI_API_KEY
from prompts.prompt_1_02 import gpt_basic_prompt

import logging

logger = logging.getLogger("app")

client = OpenAI(api_key= OPENAI_API_KEY)
prompt = gpt_basic_prompt()
response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.7,
    messages = [
        {
            "role" : "system",
            "content" : prompt["system_instruction"]
        },
        {
            "role" : "user",
            "content" : prompt["prompt"]
        }
    ]
)

logger.info(response)
logger.info("-----------------")
logger.info(response.choices[0].message.content) #response의 내용만 출력함