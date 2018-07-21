from .base import SlackObject


class SlackAttachment(SlackObject):
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

        # todo validation

        self.fallback = fallback
        self.color = color
        self.pretext = pretext
        self.author_name = author_name
        self.author_link = author_link
        self.author_icon = author_icon
        self.title = title
        self.title_link = title_link
        self.text = text
        self.fields = fields
        self.image_url = image_url
        self.thumb_url = thumb_url
        self.footer = footer
        self.footer_icon = footer_icon
        self.ts = ts

    @classmethod
    def from_dict(cls, attachment_dict):
        m = attachment_dict.copy()
        m['fields'] = []
        for f in attachment_dict['fields']:
            m['fields'].append(AttachmentField.from_dict(f))
        return cls(**m)

    def as_dict(self):
        return {
            'fallback': self.get_fallback(),
            'color': self.get_color(),
            'pretext': self.get_pretext(),
            'author_name': self.get_author_name(),
            'author_link': self.get_author_link(),
            'author_icon': self.get_author_icon(),
            'title': self.get_title(),
            'title_link': self.get_title_link(),
            'text': self.get_text(),
            'fields': self.get_fields(),
            'image_url': self.get_image_url(),
            'thumb_url': self.get_thumb_url(),
            'footer': self.get_footer(),
            'footer_icon': self.get_footer_icon(),
            'ts': self.get_ts(),
        }

    def get_fallback(self):
        return self.fallback

    def get_color(self):
        return self.color

    def get_pretext(self):
        return self.pretext

    def get_author_name(self):
        return self.author_name

    def get_author_link(self):
        return self.author_link

    def get_author_icon(self):
        return self.author_icon

    def get_title(self):
        return self.title

    def get_footer_icon(self):
        return self.footer_icon

    def get_title_link(self):
        return self.title_link

    def get_text(self):
        return self.text

    def get_fields(self):
        return [f.as_dict() for f in self.fields]

    def get_image_url(self):
        return self.image_url

    def get_thumb_url(self):
        return self.thumb_url

    def get_footer(self):
        return self.footer

    def get_ts(self):
        return self.ts


class InteractiveSlackAttachment(SlackObject):
    def as_dict(self):
        pass

    @classmethod
    def from_dict(cls, message_dict):
        pass


class AttachmentField(SlackObject):

    def __init__(self, title, value, short=True):
        self.title = title
        self.value = value
        self.short = short

    @classmethod
    def from_dict(cls, field_dict):
        return cls(**field_dict)

    def as_dict(self):
        return {
            'title': self.title,
            'value': self.value,
            'short': self.short
        }
