from rest_framework import serializers
from data_api.models import Hit


class HitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hit
        fields = ('created', 'id', 'triggered_by',
                  'area', 'note', 'rank', 'meds', 'owner')

    def create(self, validated_data):
        return Hit(**validated_data)

    def update(self, instance, validated_data):
        instance.triggered_by = validated_data.get('triggered_by',
                                                   instance.triggered_by)
        instance.area = validated_data.get('area', instance.area)
        instance.note = validated_data.get('note', instance.note)
        instance.rank = validated_data.get('rank', instance.rank)
        instance.meds = validated_data.get('meds', instance.created)
        instance.owner = validated_data.get('created', instance.owner)
        return instance

    # .save() will create a new instance.
    # serializer = HitSerializer(data=data)
    # .save() will update the existing `Hit` instance.
    # serializer = HitSerializer(Hit, data=data)
