from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from model_mommy import mommy


class TestPublication(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_read_publication(self):
        cat = [mommy.make("blog.category")]
        publication = mommy.make("blog.publication", _fill_optional=True, categories=cat)
        response = self.client.get("/blog/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data[0]
        self.assertEqual(data.get("date", None), publication.date)
        self.assertEqual(data.get("title", None), publication.title)
        self.assertTrue(data.get("image", None))
        self.assertEqual(data.get("content", None), publication.content)
        self.assertEqual(data.get("all_content", None), publication.all_content)
        self.assertEqual(data.get("link", None), publication.link)
        self.assertEqual(data.get("likes", None), publication.likes)
        self.assertEqual(data.get("comments", None), publication.comments)
        categories = data.get("categories", None)
        self.assertTrue(categories)
        obj_category = publication.categories.first()
        self.assertEqual(categories[0].get("slug"), obj_category.slug)
        self.assertEqual(categories[0].get("name"), obj_category.name)
