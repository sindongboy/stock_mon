# coding: utf-8

import os 
from openai import OpenAI

class LLM:
    api_key = None
    def __init__(self, model_choice):
        self.model_choice = model_choice.lower()
        self.client = self._initialize_client()

    def _initialize_client(self):
        if self.model_choice == "deepseek":
            self.api_key = os.getenv("DEEPSEEK_API_KEY")
            return OpenAI(api_key=self.api_key, base_url="https://api.deepseek.com/v1")
        elif self.model_choice == "openai":
            self.api_key = os.getenv("OPENAI_API_KEY")
            return OpenAI(api_key=self.api_key)
        else:
            raise ValueError("Invalid model choice. Choose 'deepseek' or 'openai'.")

    def chat(self, messages):
        model_name = "deepseek-chat" if self.model_choice == "deepseek" else "gpt-4o-mini"
        response = self.client.chat.completions.create(
            model=model_name,
            messages=messages,
            stream=False
        )
        return response.choices[0].message.content

def main():
    # 사용 예시
    deepseek_client = LLM("deepseek")
    gpt4o_mini_client = LLM("openai")

    deepseek_response = deepseek_client.chat([
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are the main features of DeepSeek V3?"}
    ])
    print("DeepSeek V3 response:", deepseek_response)

    gpt4o_mini_response = gpt4o_mini_client.chat([
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are the main features of GPT-4o Mini?"}
    ])
    print("GPT-4o Mini response:", gpt4o_mini_response)


if __name__ == "__main__":
    main()