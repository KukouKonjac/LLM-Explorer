import os
from openai import OpenAI

API_KEY = os.getenv("DEEPSEEK_API_KEY_GUGA")
if API_KEY is None: raise RuntimeError("环境变量 DEEPSEEK_API_KEY_GUGA 不存在！")

print(f"API Key: {API_KEY[:8]}********")

client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com/v1")

response = client.chat.completions.create(model="deepseek-chat", messages=[{"role":"system","content":"You are a helpful assistant."},{"role":"user","content":"请回复：DeepSeek API连接成功。"}], temperature=0)

print("\n========== Response ==========")
print(response.choices[0].message.content)

if response.usage:
    print("\n========== Usage ==========")
    print(f"Prompt Tokens     : {response.usage.prompt_tokens}")
    print(f"Completion Tokens : {response.usage.completion_tokens}")
    print(f"Total Tokens      : {response.usage.total_tokens}")

print("\n✓ DeepSeek API 测试成功！")