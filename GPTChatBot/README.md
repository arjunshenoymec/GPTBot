# GPTChatBot

This app takes the shape of a bot which you can directly converse with. When a user sends a Direct Message to the bot, it passes the text as a prompt to the `openai.Completions` endpoint and passes the responses back to the user. 

## App Scopes
The following are the scopes that the bot requires for functioning

* `im:history` - This allows the bot to access meesages and other contents in Direct Messages. 

## Event Subscriptions
This bot subscribes to the following events.

* `message.im` - The event corresponds to a message sent in the DM channel to the bot. 

## Other setup 

* Enabling users to send DMs: In the `App Home` section of the app, enable the app to be online all the time and also enable the option to allow users to send slash commands and messages from the message tab. 

* Setting the app level token: Provide a token for the app with write permissions (`connections:write`)


This app communicates to the server via `SocketMode`. [SocketMode](https://api.slack.com/apis/connections/socket) is usually used for testing and enables us to skip various configuration steps when we want to focus on the functionality of the app. 

