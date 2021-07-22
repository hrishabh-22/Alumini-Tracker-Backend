from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = Project
        fields = ('id', 'author', 'title',
                  'description', 'image', 'github_url')
