from slacky import settings
from slackclient import SlackClient


class SlackMessageSender(object):

    def send_message(self, message, channel, **kwargs):
        sc = SlackClient(settings.SLACK_APP_ACCESS_TOKEN)

        response = sc.api_call(
            'chat.postMessage',
            channel=channel,
            **message.asdict
        )
        return response
