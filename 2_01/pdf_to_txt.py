# pdf 파일을 텍스트 파일로 변환

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import OpenAI
from config.const import OPENAI_API_KEY
from config.log_config import logger
import streamlit as st
import pymupdf

pdf_file_path = "2_01/data/1810.04805v2.pdf"

doc = pymupdf.open(pdf_file_path)

full_text = ""

for page in doc:
    text = page.get_text()
    full_text +=text

pdf_file_name = os.path.basename(pdf_file_path)
pdf_file_name = os.path.splitext(pdf_file_name)[0] # 확장자 제거

#output 폴더에 full_text 내용을 텍스트 파일 형식으로 저장
txt_file_path = f"2_01/output/{pdf_file_name}.txt"
with open(txt_file_path, 'w', encoding='utf-8') as f:
    f.write(full_text)


def extract_txt(file_path:str):
    pdf_file_path = file_path

    doc = pymupdf.open(pdf_file_path)

    full_text = ""

    for page in doc:
        text = page.get_text()
        full_text +=text

    pdf_file_name = os.path.basename(pdf_file_path)
    pdf_file_name = os.path.splitext(pdf_file_name)[0] # 확장자 제거

    #output 폴더에 full_text 내용을 텍스트 파일 형식으로 저장
    txt_file_path = f"2_01/output/{pdf_file_name}.txt"
    with open(txt_file_path, 'w', encoding='utf-8') as f:
        f.write(full_text)