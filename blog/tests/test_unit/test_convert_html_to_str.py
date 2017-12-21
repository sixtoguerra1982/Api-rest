from rest_framework.test import APITestCase
from blog.tests.utils.data import html_data, iframe_data
from blog.utils import extract_text_from_html
import re


class TestConvertHTML(APITestCase):

    def test_convert_html_to_str(self):
        result_data = extract_text_from_html(html_data)
        tags = re.findall("(<\w+>)", result_data)
        self.assertEqual(len(tags), 0)

    def test_convert_p_to_line_break(self):
        result_data = extract_text_from_html(html_data)
        result = re.findall("(\n\r)", result_data)
        self.assertNotEqual(len(result), 0)

    def test_convert_iframe_to_link(self):
        result_data = extract_text_from_html(html_data)
        result = re.findall("(<iframe.*>)", result_data)
        self.assertEqual(len(result), 0)




