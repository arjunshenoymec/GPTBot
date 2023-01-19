import openai
import os

__all__ = ('get_open_ai_response')
# Adding the openai key
openai_key = os.environ.get("OPENAI_TOKEN")
openai.api_key = openai_key

def get_open_ai_response(prompt):
    """
    """
    if prompt:
        response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=prompt,
                    temperature=0.3,
                    max_tokens=2084,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0)
        if response.choices:
            return [choice.text for choice in response.choices]
        else:
            return []
    
    