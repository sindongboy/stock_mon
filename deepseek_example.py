# coding: utf-8

import os
from openai import OpenAI

api_key = os.getenv('DEEPSEEK_API_KEY')
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

def test():
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Hello"},
        ],
        stream=False
    )

    print(response.choices[0].message.content)

def main():
    test()


if __name__ == "__main__":
    main()