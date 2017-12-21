from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from model_mommy import mommy


class TestComment(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_set_comment(self):
        publication = mommy.make("blog.publication")
        data = {
            "comment": "Test comment"
        }
        url = "/blog/{}/set-comment/".format(publication.id)
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_read_comments(self):
        publication = mommy.make("blog.publication")
        mommy.make("blog.comment", publication=publication, _quantity=21)
        url = "/blog/{}/get-comments/".format(publication.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        response = self.client.get("{}?page=1".format(url))
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertIn("results", response.data.keys(), response.data)
        self.assertEqual(len(response.data.get("results")), 20, response.data)
