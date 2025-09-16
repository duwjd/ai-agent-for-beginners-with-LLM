def gpt_basic_prompt():
    system_instruction = "You are a helpful assistant"
    prompt="안녕? 서울의 수도는 어디야?"
    return {"system_instruction" : system_instruction, "prompt" : prompt}