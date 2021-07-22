from rest_framework import viewsets
from .models import AllMessage
from .serializers import AllMessageSerializer
from rest_framework.permissions import AllowAny


class AllMessageViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}
    queryset = AllMessage.objects.all()
    serializer_class = AllMessageSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]

        except KeyError:
            return [permission() for permission in self.permission_classes]
