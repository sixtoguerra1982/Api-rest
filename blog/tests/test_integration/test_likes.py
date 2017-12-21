from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from model_mommy import mommy


class TestLike(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_set_like(self):
        publication = mommy.make("blog.publication")
        url = "/blog/{}/set-like/".format(publication.id)
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

