from django.db.models import fields
from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import AllMessage


class AllMessageSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = AllMessage
        fields = ('id', 'sender', 'receiver', 'description', 'image')
