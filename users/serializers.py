from django.contrib.auth.models import User, Group
from rest_framework import serializers

from data_api.models import Hit


class UserSerializer(serializers.HyperlinkedModelSerializer):
    pains = serializers.PrimaryKeyRelatedField(many=True,
                                               queryset=Hit.objects.all())
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'pains')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Group
            fields = ('url', 'name')
