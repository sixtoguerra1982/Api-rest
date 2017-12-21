from django.db import models
from django.db.models import deletion


class Publication(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=140)
    image = models.URLField()
    content = models.TextField()
    all_content = models.TextField()
    original_all_content = models.TextField()
    link = models.URLField(blank=True, null=True)
    comments = models.URLField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    categories = models.ManyToManyField("blog.Category")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.TextField()
    publication = models.ForeignKey("blog.Publication",
                                    related_name="get_comments",
                                    on_delete=deletion.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}...".format(self.comment[:100])


class Like(models.Model):
    """
    This entity was created for make more extensible this functionality.
    """
    publication = models.ForeignKey("blog.Publication",
                                    related_name="get_likes",
                                    on_delete=deletion.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.publication.title
