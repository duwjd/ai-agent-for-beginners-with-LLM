from openai import OpenAI
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.const import OPENAI_API_KEY
from config.log_config import logger
from prompts.prompt_1_03 import gpt_mirror_in_snow_prompt

client = OpenAI(api_key= OPENAI_API_KEY)
prompt = gpt_mirror_in_snow_prompt()
response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.9,
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