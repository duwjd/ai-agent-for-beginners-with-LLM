from openai import openai
from config.const import OPENAI_API_KEY
from prompts.prompt_1_02 import gpt_basic_prompt

client = OpenAI(OPENAI_API_KEY)
prompt = gpt_basic_prompt()
response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.7,
    messages = [
        {
            "role" : "system",
            "content" : prompt
        }
    ]
)