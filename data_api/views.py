from rest_framework import viewsets
from data_api.models import Hit
from data_api.serializers import HitSerializer


class HitViewSet(viewsets.ModelViewSet):
    queryset = Hit.objects.all()
    serializer_class = HitSerializer
