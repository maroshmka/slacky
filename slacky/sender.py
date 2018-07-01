from slackclient import SlackClient


class SlackMessageSender(object):

    def __init__(self, token):
        self.token = token

    def _get_response(self, **kwargs):
        sc = get_client(self.token)
        return sc.api_call(**kwargs)

    # todo - maybe allow to override token with kwargs ?
    def send(self, message, channel):
        return self._get_response(
            method='chat.postMessage',
            channel=channel,
            **message.as_dict()
        )

    def send_ephemeral(self, message, channel, user_id):
        return self._get_response(
            method='chat.postEphemeral',
            channel=channel,
            user=user_id,
            **message.as_dict()
        )

    # todo - maybe create shortcuts, like, update last etc.
    def update(self, message, channel, ts):
        return self._get_response(
            method='chat.update',
            channel=channel,
            ts=ts,
            **message.as_dict()
        )

    def delete(self, channel, ts):
        return self._get_response(
            method='chat.delete',
            channel=channel,
            ts=ts,
        )


clients = {}


def get_client(token):
    global clients
    sender = clients.get(token)
    if not sender:
        clients[token] = sender = SlackClient(token)
    return sender
