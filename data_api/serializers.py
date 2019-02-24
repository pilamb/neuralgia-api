from rest_framework import serializers
from data_api.models import Hit


class HitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hit
        fields = ('created', 'id', 'triggered_by',
                  'area', 'note', 'rank', 'meds')
