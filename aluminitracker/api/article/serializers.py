from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = Article
        fields = ('id', 'author', 'title', 'description', 'image')
