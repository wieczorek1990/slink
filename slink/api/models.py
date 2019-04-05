import random
import string

from django.conf import settings
from django.db import models

from api import validators


class Link(models.Model):
    original_link = models.CharField(max_length=2048, unique=True,
                                     validators=validators.URL_VALIDATORS)
    short_link = models.CharField(max_length=2048, unique=True,
                                  validators=validators.URL_VALIDATORS)
    number_of_visits = models.IntegerField(default=0)

    def __str__(self):
        return '{} -> {}'.format(self.short_link, self.original_link)

    @classmethod
    def create(cls, host, original_link):
        short_link = cls.generate_short_link(host)
        link = cls(original_link=original_link, short_link=short_link)
        return link

    @classmethod
    def generate_short_link(cls, host):
        done = False
        while not done:
            link_id = ''.join(random.choice(string.ascii_lowercase +
                                            string.digits)
                              for _ in range(settings.LINK_LENGTH))
            short_link = cls.get_short_link(host, link_id)
            link = Link.objects.filter(short_link=short_link).first()
            done = not bool(link)
        return short_link

    @staticmethod
    def get_short_link(host, link_id):
        return 'http://{}/links/{}'.format(host, link_id)

    def visited(self):
        self.number_of_visits += 1
        self.save()
