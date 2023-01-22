# OpeanAI based productivity bots

- [Introduction](#OpeanAI-based-productivity-bots)
- [Prerequisites](#pre-requisites)
    - [Access to slack workspace](#access-to-a-slack-workspace)
    - [openAI Access](#openai-access-tokens)
- [Setting up a slack app](#setting-up-a-slack-app)
    - [Slack app scope](#slack-app-scopes)
    - [Event Subscription](#event-subscription)
- [Repo Structure](#structure-of-the-repo)
- [Contribute](#contributing)
- [References](#references)

This repo details the code and instructions to setup various slack bots that improve user productivity by interactiving with various openai endpoints. 

## Pre-requisites 
### Access to a slack workspace
You would admin access to either your own slack workspace or your organization's slack workspace. This is needed so that you can create and install apps. Click [here](https://slack.com/intl/en-gb/help/articles/206845317-Create-a-Slack-workspace#create-a-workspace) for instructions to setup your own slack workspace if necessary (You can setup your own slack workspaces for free, however there will be limitations on aspects like max file size that can be uploaded, the retention of messages in channels and DMs etc.)

### OpenAI Access tokens
In order to make calls to openai endpoints, you require an access token. This might require you to setup a paid account on OpenAI Check [here](https://beta.openai.com/account/billing/overview) for more details about the pay-per-usage scheme. 

## Setting up a slack app
In this section we describe the steps for setting up a skeleton slack app and also the other permissions and aspects required to build the bots we are focusing on. 

Specific details about the permissions and special steps required for each app is mentioned in the corresponding app's readme.

Setup a basic slack app by visiting the slack [api](https://api.slack.com/apps?new_app=1) page. Click on `Create New App`. Follow the necessary prompts (In the case of the apps in this repo, I had set the apps `From Scratch`). Once you provide the name for the app and select the workspace in which you would want to deploy and test the app. You will reach the homepage of the app. We will focus on configuring certain permissions reuired for the app. 

### Slack app scopes
Scopes give the app permission to do things (for example, post messages) in the workspace. You can select the scopes to add to your app by navigating over to the `OAuth & Permissions` sidebar in the slack app's homepage. 

The specific bot scopes required for each app is mentioned in the corresponding Readme. 

Take note that any change to the scopes of the app would require the app to be re-installed in the corresponding workspace for the change to take effect. 

### Event subscription
Typically, a slack app functions by acting on certain events (a user joinging a channel, a message put in the channel, someone uploads a file etc.). The specific event that your app should listen for and respond to can be set by going to the `Event Subscriptions` section in the slack app's homepage. 

The specific events each of the app acts on in this case is listed out in the corresponding Readme. 

While subscribing for events, you have two choices. You can

- Specify a Request URL (which should get resolved to the server where you will be running the slack application code) appending the URL with `/slack/events`. 
or 
- You can run the app in [socket mode](https://api.slack.com/apis/connections/socket)

The code to intiialise and start the slack app is differs when it runs on socket mode vs when it is run as a server.

## Structure of the repo
This repo consits of code developed for various different apps (in some cases, the same app might be implmented in different manners. In such cases, I have mostly created a separate directory for each different approach). 

Each directory in turn consits of
- A README file which lists out a description of the app, the permissions it requires and the events it subscribes to.
- A config.py file which lists out the necessary config for the app
- app.py file which is the main code for the app
The directory might contain other files if necessary. 

Other than directories for each of the apps, A `utils` directory is also present which contains resources shared by the apps. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## References
- https://api.slack.com/start/building/bolt-python
- https://api.slack.com/apis/connections/socket
- https://ngrok.com/docs/getting-started (I was using ngrok as a proxy before deploying the app in a proper envrionment)
- https://api.slack.com/events
- https://slack.dev/bolt-python/concepts#commands
- https://api.slack.com/tutorials/tracks/responding-to-app-mentions
- https://beta.openai.com/docs/introduction

