import openai

__all__ = ("OpenAIClient")

class OpenAIClient(object):
    """
    """
    def __init__(self, token: str, param_mapping: dict):
        openai.api_key = token
        self._params = param_mapping

    def get_responses(self, prompt):
        """
        """
        if prompt:
            self._params["prompt"] = prompt
            response = openai.Completion.create(**self._params)
            if response.choices:
                return [choice.text for choice in response.choices]
            else:
                return []