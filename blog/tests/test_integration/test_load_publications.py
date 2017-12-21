from unittest import mock
from rest_framework.test import APITestCase
from blog.tests.utils.data import response_data
from blog.models import Publication
from blog.services import load_publications


class Mock:

    status_code = 200

    @staticmethod
    def json():
        return response_data


class TestLoadPublication(APITestCase):

    @mock.patch("blog.services.requests.get")
    def test_load_publications(self, get):
        get.return_value = Mock

        load_publications()
        count_pub = Publication.objects.count()
        self.assertEqual(count_pub, 12)



