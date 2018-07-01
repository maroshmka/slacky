from slacky.attachment import SlackAttachment
from slacky.base import SlackObject
from .sender import SlackMessageSender


class SlackMessage(SlackObject):

    def __init__(self, text=None, attachments=None):
        self.text = text or ''
        self.attachments = attachments or []

    def send(self, channel, token):
        sender = SlackMessageSender(token)
        return sender.send(self, channel)

    def send_ephemeral(self, channel, user_id, token):
        sender = SlackMessageSender(token)
        return sender.send_ephemeral(self, channel, user_id)

    def update(self, channel, ts, token):
        sender = SlackMessageSender(token)
        return sender.update(self, channel, ts)

    def delete(self, channel, ts, token):
        sender = SlackMessageSender(token)
        return sender.delete(channel, ts)

    def get_text(self):
        return self.text

    def get_attachments(self):
        return [
            a.as_dict() for a in self.attachments
        ]

    def copy(self):
        pass

    @classmethod
    def from_dict(cls, message_dict):
        m = message_dict.copy()
        m['attachments'] = []
        for a in message_dict['attachments']:
            m['attachments'].append(SlackAttachment.from_dict(a))
        return cls(**m)

    def as_dict(self):
        return {
            'text': self.get_text(),
            'attachments': [a.as_dict() for a in self.attachments]
        }
