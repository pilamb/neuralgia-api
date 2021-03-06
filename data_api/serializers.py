from rest_framework import serializers
from data_api.models import Hit


class HitSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Hit
        fields = ('created', 'id', 'triggered_by',
                  'area', 'note', 'rank', 'meds', 'owner')

