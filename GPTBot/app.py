import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from utils.openai.openai_client import OpenAIClient
from utils.buffer.buffer import ContextBuffer
from config import SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET, SLACK_APP_TOKEN, OPENAI_TOKEN
from config import OPENAI_PARAM_MAPPING

app = App(token=SLACK_BOT_TOKEN,
          signing_secret=SLACK_SIGNING_SECRET)

buffer = ''
openai_client = OpenAIClient(OPENAI_TOKEN, OPENAI_PARAM_MAPPING)


@app.event("message")
def handle_message_events(say, message):
    print(message)
    prompt = message['text']
    responses = openai_client.get_responses(prompt)
    for response in responses:
        say(response)
        # buffer = buffer + response

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))