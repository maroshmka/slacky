class Attachment(object):
    """

    :param fallback: 'Required plain-text summary of the attachment.',
    :param color': '#2eb886',
    :param pretext: 'Optional text that appears above the attachment block',
    :param author_name: 'Bobby Tables',
    :param author_link: 'http://flickr.com/bobby/',
    :param author_icon: 'http://flickr.com/icons/bobby.jpg',
    :param title: Slack API Documentation,
    :param title_link: https://api.slack.com/,
    :param text: Optional text that appears within the attachment,
    :param fields: list of Fields,
    :param image_url: http://my-website.com/path/to/image.jpg,
    :param thumb_url: http://example.com/path/to/thumb.png,
    :param footer: Slack API,
    :param footer_icon: https://platform.slack-edge.com/img/default_application_icon.png,
    :param ts: 123456789

    """

    def __init__(self, fallback=None, color=None, pretext=None, author_name=None, author_link=None,
                 author_icon=None, title=None, title_link=None, text=None, fields=None,
                 image_url=None,
                 thumb_url=None, footer=None, footer_icon=None, ts=None):
        self.fallback = 'Required plain-text summary of the attachment.'
        self.color = ''
        self.pretext = ''
        self.author_name = ''
        self.author_link = ''
        self.author_icon = 'http://flickr.com/icons/bobby.jpg'
        self.title = 'Slack API Documentation'
        self.title_link = 'https://api.slack.com/',
        self.text = 'Optional text that appears within the attachment',
        self.fields = list()


class InteractiveAttachment(object):
    pass


class Field(object):
    FIELDS = ('title', 'value', 'short', '_data')

    def __init__(self, title, value, short=True):
        self._data = {'title': title, 'value': value, 'short': short}
        # self.title = title,
        # self.value = value
        # self.short = short
        # super().__init__(**kwargs)

    def __getattr__(self, item):
        if item not in Field.FIELDS:
            raise KeyError
        return self.__dict__['_data'][item]

    def __setattr__(self, key, value):
        if key == '_data':
            self.__dict__[key] = value

        # todo - maybe remove - protect delete and empty values
        elif key not in Field.FIELDS:
            raise AttributeError(
                '`Field` has no attribute `{k}`. Choices are - {fields}'.format(k=key,
                                                                                fields=Field.FIELDS))

        self.__dict__['_data'][key] = value

    def __repr__(self):
        return '{ \'title\': %s, asddsa:bbb}' % (self.title)
