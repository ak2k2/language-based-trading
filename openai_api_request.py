# Written by Armaan Kapoor on 12-26-2022

import os

import openai

openai.api_key = os.environ["OPENAI_API_KEY"]


class make_openai_request:

    def __init__(self):
        self.prompt = ""
        self.temperature = 0.0
        self.frequency_penalty = 0.0
        self.stop = None


    def request(self, prompt):
        self.prompt = prompt
        self.tokensout = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.prompt,
            temperature=self.temperature,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=0.0,
            stop=self.stop,
        )
        return self.tokensout["choices"][0]["text"].strip()