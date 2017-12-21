from rest_framework.test import APITestCase
from blog.tests.utils.data import response_data
from blog.services import ProcessDataService


class TestProcessData(APITestCase):

    def test_process_data(self):

        data = response_data.get("items")[0]
        serializer = ProcessDataService(data=data)

        self.assertTrue(serializer.is_valid(), serializer.errors)

        serializer.save()
        publication = serializer.instance

        self.assertEqual(data.get("title", None), publication.title)
        self.assertTrue(data.get("image", None))

        all_content = data.get("all_content", None)
        self.assertNotEqual(all_content, publication.all_content)
        self.assertEqual(data.get("link", None), publication.link)
        self.assertEqual(data.get("comments", None), publication.comments)

        categories = data.get("categories", None)
        self.assertTrue(categories)

        obj_category = publication.categories.first()
        self.assertEqual(categories[0].get("slug"), obj_category.slug)
        self.assertEqual(categories[0].get("name"), obj_category.name)

        content = data.get("content", None)
        self.assertEqual(content.strip(), publication.content)




