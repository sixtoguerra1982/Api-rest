from utils.base.viewsets import ModelCrudViewSet
from blog import models as blog_models
from blog import serializers as blog_serializers
from rest_framework.decorators import detail_route
from blog import services as blog_services
from rest_framework.response import Response
from rest_framework import status
from blog import utils
from django.utils.translation import ugettext_lazy as _


class PublicationsViewSet(ModelCrudViewSet):
    queryset = blog_models.Publication.objects.all()
    serializer_class = blog_serializers.PublicationSerializer
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        msg = _("Method not allowed")
        return Response(msg, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @detail_route(methods=['post'], url_path='set-comment')
    def set_comment(self, request, *args, **kwargs):
        data = request.data.copy()
        data['publication'] = self.get_object().id
        service = blog_services.CommentService(data=data)
        service.is_valid(raise_exception=True)
        service.save()
        return Response(data=service.data, status=status.HTTP_201_CREATED)

    @detail_route(methods=['post'], url_path='set-like')
    def set_like(self, request, pk=None):
        instance = self.get_object()
        utils.set_like(instance)
        return Response(status=status.HTTP_201_CREATED)

    @detail_route(methods=['get'], url_path='get-comments')
    def get_comments(self, request, pk=None):
        """
        Return a list of comments for the selected publication

        if the 'page' param is received, the response will be rendered
        with the pagination system.

        """
        instance = self.get_object()
        queryset = instance.get_comments.all().order_by('-date')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = blog_serializers.CommentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = blog_serializers.CommentSerializer(queryset, many=True)
        return Response(serializer.data)






