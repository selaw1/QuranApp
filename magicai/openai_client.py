


import os

from openai import OpenAI

from magicai.models import ResponseData


class OpenAiClient():
    # defaults to getting the key using os.environ.get("OPENAI_API_KEY")
    # if you saved the key under a different environment variable name, you can do something like:
    # client = OpenAI(
    #   api_key=os.environ.get("CUSTOM_ENV_NAME"),
    # )
    client = OpenAI()

    @classmethod
    def send_prompt(cls, user_prompt):
        completion = cls.client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a religious Muslim Scholar, skilled in helping people feel better by quoting verses from the Quran based on their situation."},
            {"role": "user", "content": f"ONLY reply with a Quran verse. You can include more than one verse. The verse MUST be in Arabic, and translated in English in a new line. Never include the situation in the answer. The Situation:{user_prompt}"}
        ]
        )

        response_data = ResponseData(
            quran_res=completion.choices[0].message.content,
            completion_tokens=completion.usage.prompt_tokens,
            total_tokens=completion.usage.total_tokens,
            prompt_tokens=completion.usage.completion_tokens,
            gpt_model=completion.model
        )
        response_data.save()
        return response_data