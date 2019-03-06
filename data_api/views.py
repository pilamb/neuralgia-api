from rest_framework import viewsets, permissions

from data_api.models import Hit
from data_api.permissions import IsOwnerOrReadOnly
from data_api.serializers import HitSerializer


class HitViewSet(viewsets.ModelViewSet):
    queryset = Hit.objects.all()
    serializer_class = HitSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
