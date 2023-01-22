import openai

__all__ = ("OpenAIClient")

class OpenAIClient(object):
    """
    """
    def __init__(self, token):
        openai.api_key = token

    def get_responses(self, prompt):
        """
        """
        if prompt:
            response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=prompt,
                        temperature=0.3,
                        max_tokens=3000,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0)
            if response.choices:
                return [choice.text for choice in response.choices]
            else:
                return []