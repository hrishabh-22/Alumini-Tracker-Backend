from rest_framework import viewsets
from .models import Recommendation
from .serializers import RecommendationSerializer
from rest_framework.permissions import AllowAny


class RecommendationViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]

        except KeyError:
            return [permission() for permission in self.permission_classes]
