# GPTBot

This app is similar to [GPTChatBot](../GPTChatBot/README.md). When a user sends a Direct Message to the bot, it passes the text as a prompt to the `openai.Completions` endpoint and passes the responses back to the user. 

Unlike GPTChatBot this communicates with a server to relay events and obtain responses. Therefore, a few additional configurations are required here. 

## App Scopes
The following are the scopes that the bot requires for functioning

* `im:history` - This allows the bot to access meesages and other contents in Direct Messages.
* `chat:write` - This lets the bot send direct messages as `@GPTBot`.


## Event Subscriptions
This bot subscribes to the following events.

* `message.im` - The event corresponds to a message sent in the DM channel to the bot.

The difference here is that unlike GPTChatBot which uses `SocketMode`, this app communicates via a server hence, we have to specify a Request URL. When an event the app is subscribed to occurs, slack sends the event metadata to the Request URL (we have to append `/slack/event` to the URL).

## Other setup 

* Enabling users to send DMs: In the `App Home` section of the app, enable the app to be online all the time and also enable the option to allow users to send slash commands and messages from the message tab. 

* Setting the app level token: Provide a token for the app with write permissions (`connections:write`)
