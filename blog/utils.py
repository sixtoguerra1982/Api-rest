import re
from datetime import datetime

from django.db import transaction

from blog.models import Like
from parser.html_parsers import HTMLParser

DEFAULT_BLOG_LOADER = "https://www.teleton.cl/feed/?json"

TRANSLATED_MONTHS = {
    "enero": "January",
    "febrero": "February",
    "marzo": "March",
    "abril": "April",
    "mayo": "May",
    "junio": "June",
    "Julio": "July",
    "agosto": "August",
    "septiembre": "September",
    "octubre": "October",
    "nobiembre": "November",
    "diciembre": "December",
}


def set_like(instance):
    with transaction.atomic():
        """
        This transaction ensures that a Like instance 
        is not saved without increasing the 'like' 
        parameter of the instance, or vice versa.
        """
        Like.objects.create(publication=instance)
        instance.likes += 1
        instance.save()


def convert_month_date(date_string):
    """
    Converts the date into a readable date to the datetime package.
    :param date_string: i.e: 7 diciembre, 2017
    :return: 7 December, 2017
    """
    month = re.findall("\d+ (\w+), \d+", date_string)[0]
    date_converted = re.sub(month, TRANSLATED_MONTHS[month], date_string)
    return date_converted


def convert_date(fecha):
    """
    convert string to datetime

    :param fecha: i.e: 7 December, 2017
    :return: datetime object
    """
    fecha = convert_month_date(fecha)
    date = datetime.strptime(fecha, "%d %B, %Y")
    return date


def extract_text_from_html(html_all_content):
    text = HTMLParser(html_all_content)
    return text.data
