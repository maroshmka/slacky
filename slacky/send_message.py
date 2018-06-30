from slackclient import SlackClient
from slacky import settings

sc = SlackClient(settings.SLACK_APP_ACCESS_TOKEN)

sc.api_call(
    'chat.postMessage',
    channel='CBH2Z8SDB',
    text='Hello from Python! :tada:'
)
