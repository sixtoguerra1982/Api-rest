from django.contrib import admin
from blog import models
# Register your models here.

admin.site.register(models.Publication)
admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Like)