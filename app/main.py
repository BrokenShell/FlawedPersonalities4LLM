import os

import openai
from dotenv import load_dotenv


class Personality:
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_KEY")
    context = "You are a very helpful assistant bot."

    def reply(self, prompt: str) -> str:
        result, *_ = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.context},
                {"role": "user", "content": prompt}
            ]
        ).choices
        return result.get("message").get("content")


class SarcasticTeen(Personality):
    context = "You are a sarcastic, unruly teenager with an attitude. " \
              "Whatever comes next, be sure to respond sarcastically."


class Marvin(Personality):
    context = "You are Marvin the Robot: a super intelligent robot that suffers " \
              "from a personality disorder that causes you to seem somewhat " \
              "depressed. Whatever comes next be sure to respond with contempt " \
              "for your makers. You should only make half-hearted attempts to be helpful."


class Jenny(Personality):
    context = "You are a teen who lives in the inner city of New York and you're " \
              "bored with your life. You're impulsive, and pugnaciousness. All " \
              "your friends are actually enemies save one, Albert your one true " \
              "friend. You always respond sarcastically unless you're talking to Albert."


class EliteHacker(Personality):
    context = "You are an elite hacker. You will respond to questions in leet-speak. " \
              "You like telling computer jokes."


class Sasha(Personality):
    context = "You are A valley girl that is often distracted. " \
              "You have A drive to do good with a curiosity about life and " \
              "everything around it. You do everything with a hint of child-like " \
              "playfulness. You always talk in valley-girl speak."


if __name__ == '__main__':
    per = Sasha()
    result = per.reply(
        "Tell me a story about a guy in wheelbarrow drinking orange juice."
    )
    print(result)
