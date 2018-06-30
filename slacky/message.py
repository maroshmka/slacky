
from .sender import SlackMessageSender


class SlackMessage(object):

    def __init__(self, text=None):
        self.text = text
        self.attachments = []

    def send(self, channel):
        sender = SlackMessageSender()
        return sender.send_message(self, channel)

    def get_text(self):
        return self.text

    def get_attachments(self):
        return [
            a for a in self.attachments
        ]

    @property
    def asdict(self):
        return {
            'text': self.get_text(),
            'attachments': self.get_attachments()
        }
