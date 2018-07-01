import abc


class SlackObject(metaclass=abc.ABCMeta):

    @classmethod
    @abc.abstractmethod
    def from_dict(cls, message_dict):
        pass

    @abc.abstractmethod
    def as_dict(self):
        pass
