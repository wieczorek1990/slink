from unittest import mock

from django import test
from django import urls

from api import models


class TestCase(test.TransactionTestCase):
    def setUp(self):
        self.host = 'localhost'
        self.link_id = 'abcd1234'


class ApiTestCase(TestCase):
    def test_get_link_get(self):
        response = self.client.get(urls.reverse('get_link'))
        self.assertEqual(response.status_code, 200)

    @mock.patch('api.helpers.get_host')
    def test_get_link_post(self, mock_get_host):
        mock_get_host = self.host

        response = self.client.post(urls.reverse('get_link'),
                                    {'link': 'https://www.google.com'})
        self.assertEqual(response.status_code, 201)

        response = self.client.post(urls.reverse('get_link'),
                                    {'link': 'https://www.google.com'})
        self.assertEqual(response.status_code, 200)

    @mock.patch('api.helpers.get_host')
    def test_redirect_link(self, mock_get_host):
        mock_get_host = self.host

        models.Link.create(self.host, self.link_id).save()
        response = self.client.get(urls.reverse('redirect_link',
                                   kwargs={'link_id': self.link_id}))
        self.assertEqual(response.status_code, 302)


class LinkTestCase(TestCase):
    def test_genearte_short_link(self):
        link_a, link_b = (models.Link.generate_short_link(self.host)
                          for _ in range(2))
        self.assertNotEqual(link_a, link_b)

    def test_get_short_link(self):
        result = models.Link.get_short_link(self.host, self.link_id)
        self.assertEqual(result,
                         'http://localhost/links/abcd1234')
