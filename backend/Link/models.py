import os
import logging
from base64 import urlsafe_b64encode
from django.db import models, utils
from django.contrib.sessions.models import Session
from django.conf import settings

logger = logging.getLogger(__name__)

assert settings.LENGTH_SHORT_FORM > 4, 'suspiciously short length form'


def code_generator(size=settings.LENGTH_SHORT_FORM):
    return urlsafe_b64encode(os.urandom(size)).decode('utf-8')


class Resource(models.Model):
    short_link = models.CharField(primary_key=True, max_length=16, default=code_generator,
                                  unique=True, null=False, blank=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    source = models.URLField(max_length=256)

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
        except utils.IntegrityError:
            logger.warning('Detected conflict short links of resource')

            self.short_link = code_generator()
            super().save(*args, **kwargs)
