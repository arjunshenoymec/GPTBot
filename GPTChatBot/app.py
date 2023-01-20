import os
from collections import deque
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from utils.openai.openai_util import get_open_ai_response
from utils.buffer.buffer import ContextBuffer

max_buffer_length = int(os.environ["MAX_CONTEXT_BUFFER_LEN"])
# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])
buffer = ContextBuffer(max_buffer_length)


@app.event("message")
def event_test(say, message):
    print(message)
    global buffer
    prompt = str(buffer) + message['text']
    responses = get_open_ai_response(prompt)
    for response in responses:
        say(response)
        buffer = buffer + response

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()