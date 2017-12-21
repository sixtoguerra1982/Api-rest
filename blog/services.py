import requests
from rest_framework import serializers
from blog import models as blog_models
from blog.utils import (DEFAULT_BLOG_LOADER, convert_date,
                        extract_text_from_html)
import logging

logger = logging.getLogger(__name__)


class CommentService(serializers.ModelSerializer):

    class Meta:
        model = blog_models.Comment
        fields = ('comment', 'publication',)


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = blog_models.Category
        fields = '__all__'


class ProcessDataService(serializers.ModelSerializer):
    fecha = serializers.CharField(required=True)
    categories = CategoriesSerializer(many=True)
    date = serializers.DateField(read_only=True)
    original_all_content = serializers.CharField(required=False)

    def validate(self, attrs):
        fecha = attrs.pop("fecha")
        attrs['date'] = convert_date(fecha)
        html_all_content = attrs.get('all_content')
        attrs['original_all_content'] = html_all_content
        attrs['all_content'] = extract_text_from_html(html_all_content)
        return attrs

    class Meta:
        model = blog_models.Publication
        fields = '__all__'

    def create(self, validated_data):
        categories = validated_data.pop("categories", [])
        instance = super().create(validated_data)
        instance.save()
        models_category = blog_models.Category
        for t_category in categories:
            category, _ = models_category.objects.get_or_create(**t_category)
            instance.categories.add(category.id)
        return instance


def load_publications(model=blog_models.Publication, url=DEFAULT_BLOG_LOADER):
    """

    :param model: Publication
    :param url: The blog's url

    The parameter 'model' is received so that the method
    can be used in migrations. The accepted scheme for
    this method is the current one for the migration
    '0009_load_publications_from_blog.py'.

    """
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError as connection_error:
        logger.error(connection_error)
        return

    if response.status_code != 200:
        msg = "missing url for load publications.md"
        logger.error(msg)
        return
    items = response.json().get("items")
    ProcessDataService.Meta.model = model
    service = ProcessDataService(data=items, many=True)

    if service.is_valid():
        service.save()
    else:
        msg = "error in data coming from {}".format(url)
        logger.error(msg)
