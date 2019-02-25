from rest_framework import generics

from data_api.models import Hit
from data_api.serializers import HitSerializer


class HitList(generics.ListCreateAPIView):
    queryset = Hit.objects.all()
    serializer_class = HitSerializer


class HitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hit.objects.all()
    serializer_class = HitSerializer
