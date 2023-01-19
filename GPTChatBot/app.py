import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from utils.openai.openai_util import get_open_ai_response

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

'''
@app.command("/hello-socket-mode")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi, <@{user_id}>!")
'''

@app.event("message")
def event_test(say, message):
    print(message)
    prompt = message['text']
    responses = get_open_ai_response(prompt)
    for response in responses:
        say(response)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()