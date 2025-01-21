# coding: utf-8 

import os
import openai

class OpenAIClient:
    _instance = None
    _model = "gpt-4o-mini"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OpenAIClient, cls).__new__(cls)
            cls._instance.api_key = os.getenv("OPENAI_API_KEY")
            openai.api_key = cls._instance.api_key
        return cls._instance

    def get_completion_test(self, messages):
        try:
            response = openai.chat.completions.create(
                model=self._model,
                messages=messages
            )
            return response.choices[0].message.content
        except openai.OpenAIError as e:
            print(f"An error occurred: {e}")
            return None

    def get_summary(self, article):
        try:
            response = openai.chat.completions.create(
                model=self._model,
                messages=[{"role": "system", "content": "You are an AI Agent that Summarize given news article."},
                        {"role": "user", "content": article}]
            )
            return response.choices[0].message.content
        except openai.OpenAIError as e:
            print(f"An error occurred: {e}")
            return None

def main():
    client = OpenAIClient()
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What mountain is the highest in the world?"}
    ]
    completion = client.get_completion(model="gpt-4o-mini", messages=messages)
    if completion:
        print(completion)
    else:
        print("Failed to get completion.")

if __name__ == "__main__":
    main()