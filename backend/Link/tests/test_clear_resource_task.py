from datetime import timedelta

from django.test import TestCase
from django.contrib.sessions.backends.db import SessionStore
from Link.models import Resource
from Link.tasks import clean_old_resources


class Test(TestCase):

    def setUp(self):
        self.session = SessionStore()
        self.session.create()

    def test_remove_resources(self):
        test_resource = Resource(source='http://some_url/', session_id=self.session.session_key)
        test_resource2 = Resource(source='http://some_url2/', session_id=self.session.session_key)
        Resource.objects.bulk_create([test_resource, test_resource2])

        test_resource.created = test_resource.created - timedelta(days=31)
        test_resource.save()

        self.assertTrue(Resource.objects.filter(short_link=test_resource.short_link).exists())
        self.assertTrue(Resource.objects.filter(short_link=test_resource2.short_link).exists())

        clean_old_resources()

        self.assertFalse(Resource.objects.filter(short_link=test_resource.short_link).exists())
        self.assertTrue(Resource.objects.filter(short_link=test_resource2.short_link).exists())
