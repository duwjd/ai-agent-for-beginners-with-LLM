import sys
import os
from pdf_without_header_footer import pdf_without_header_footer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import OpenAI
from config.const import OPENAI_API_KEY
from config.log_config import logger


def summarize_txt(txt):
    client = OpenAI(api_key= OPENAI_API_KEY)
    
    system_prompt = f"""너는 다음 글을 요약하는 봇이다. 아래 글을 읽고, 저자의 문제 인식과 주장을 파악하고, 주요 내용을 한글로 요약하라. 작성해야 하는 포맷은 다음과 같다.

    # 제목

    ## 저자의 문제 인식 및 주장(500자)

    ## 저자 소개

    ============ 이하 텍스트 ============

    {txt}
    """

    logger.info(system_prompt)
    logger.info("-----------------")

    response = client.chat.completions.create(
        model = "gpt-4o",
        temperature = 0.7,
        messages = [
            {
                "role" : "system",
                "content" : system_prompt
            }
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__" :
    file_path = "2_01/data/2003.03253v1.pdf"
    txt = pdf_without_header_footer(file_path)
    summary = summarize_txt(txt)
    logger.info(summary)

    with open("2_01/output/2003.03253v1_summary.txt", 'w', encoding='utf-8') as f:
        f.write(summary)