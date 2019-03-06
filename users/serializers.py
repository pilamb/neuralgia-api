from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    pains = serializers.HyperlinkedRelatedField(many=True,
                                               read_only=True,
                                               view_name="hit-detail",
                                               lookup_field="pk")
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'pains')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
