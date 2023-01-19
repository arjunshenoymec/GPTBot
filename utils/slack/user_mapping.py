import logging
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

__all__ = ('get_user_mapping')

logger = logging.getLogger(__name__)

def get_user_mapping():
    client = WebClient(token=os.environ.get("SLACK_MENTION_BOT_BOT_TOKEN"))
    try:
        # Call the users.info method using the WebClient
        result = client.users_list()
        result_mapping = {member['real_name']: member['id'] for member in result['members']}
        return result_mapping 
    except SlackApiError as e:
        logger.error("Error fetching conversations: {}".format(e))
