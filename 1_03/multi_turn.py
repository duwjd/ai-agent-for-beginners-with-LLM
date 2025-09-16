import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import OpenAI
from config.const import OPENAI_API_KEY
from config.log_config import logger


client = OpenAI(api_key= OPENAI_API_KEY)

def get_ai_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.9,
        messages = messages
    )
    return response.choices[0].message.content

messages = [{
    "role" : "system",
    "content" : "You are a helpful assistant."
}]

while True:
    user_input = input("사용자 : ")

    if user_input =="exit":
        break
    else:
        messages.append({
            "role" : "user",
            "content" : user_input
        })

        ai_response = get_ai_response(messages)
        messages.append({
            "role" : "assistant",
            "content" : ai_response
        })
        logger.info(ai_response)