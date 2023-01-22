import os

# Slack bot token used by the bot to access various resources in the workspace
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

# Slack singing secret
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]

# Slack app token
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]

# Open ai token to access the openai endpoints
OPENAI_TOKEN = os.environ["OPENAI_TOKEN"]

# OpenAI model parameters that will be used while
# querying the openai endpoint
OPENAI_PARAM_MAPPING = {
    "model": "text-davinci-003",
    "prompt": " ",
    "temperature": 0.3,
    "max_tokens": 3000,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0
}