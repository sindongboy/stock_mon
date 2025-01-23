# coding: utf-8

import os
import openai

class OpenAICore:
    _instance = None
    _model = "gpt-4o-mini"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OpenAICore, cls).__new__(cls)
            cls._instance.api_key = os.getenv("OPENAI_API_KEY")
            openai.api_key = cls._instance.api_key
        return cls._instance

    def get_summary(self, article):
        pass