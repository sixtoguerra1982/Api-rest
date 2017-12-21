import serpy


class CategorySerializer(serpy.Serializer):
    name = serpy.Field()
    slug = serpy.Field()
    

class PublicationSerializer(serpy.Serializer):
    id = serpy.IntField()
    date = serpy.Field()
    title = serpy.Field()
    image = serpy.Field()
    content = serpy.Field()
    all_content = serpy.Field()
    link = serpy.Field()
    comments = serpy.Field()
    likes = serpy.Field()
    categories = serpy.MethodField()

    def get_categories(self, obj):
        serializer = CategorySerializer(obj.categories.all(), many=True)
        return serializer.data


class CommentSerializer(serpy.Serializer):
    comment = serpy.Field()
    date = serpy.Field()
