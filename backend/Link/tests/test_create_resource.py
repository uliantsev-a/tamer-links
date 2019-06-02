from django.test import TestCase
from django.urls import reverse
from django.contrib.sessions.backends.db import SessionStore
from Link.models import Resource
from Link.views import LinkViewSet
from rest_framework.test import APIRequestFactory


class Test(TestCase):

    def setUp(self):
        self.session = SessionStore()
        self.session.create()

    def test_ignore_session_params(self):
        data = {
            'source': 'sourceLink',
            'short_link': 'shortLink',
            'session': 'fakeSession',
        }

        factory = APIRequestFactory()
        url = reverse('link-list')

        wsgi_request = factory.post(url, data=data)
        wsgi_request.session = self.session

        list_view = LinkViewSet.as_view({'post': 'create'})
        response = list_view(wsgi_request)
        self.assertEqual(response.status_code, 201)

        resource = Resource.objects.get(short_link=response.data['short_link'])
        self.assertNotEqual(data['session'], resource.session.session_key)
        self.assertEqual(wsgi_request.session.session_key, resource.session.session_key)
