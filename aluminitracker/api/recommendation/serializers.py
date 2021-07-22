from django.db.models import fields
from rest_framework import serializers
from .models import Recommendation


class RecommendationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recommendation
        fields = ('id', 'user', 'java', 'python', 'javascript')
