# coding: utf-8 

import os
import openai

class LLMClient:
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
                messages=[{"role": "system", "content": "You are an AI Agent\
                        that Summarize given news article. and give top 5 \
                        important keywords with array format at the last sentence. when give keywords array, \
                        only give keywords array, no title or any other decorations"},
                        {"role": "user", "content": article}]
            )
            return response.choices[0].message.content
        except openai.OpenAIError as e:
            print(f"An error occurred: {e}")
            return None

    def invest_opinions(self, article):
        try:
            response = openai.chat.completions.create(
                    model=self._model,
                    messages=[{"role": "system", "content": "You are an Stock Investment Expert\
                            that give investment opinion based on the given articles. \
                            and give '+' symbol if your opinion about the stock is positive, \
                            '-' otherwise at the last sentence\
                            and also include your confidence level about your opinion from 1 to 10 scale at the last sentence. "},
                            {"role": "user", "content": article}]
                )
            return response.choices[0].message.content
        except openai.OpenAIError as e:
            print(f"An error occurred: {e}")
            return None


def main():
    client = LLMClient()
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