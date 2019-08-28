from django.contrib.auth.models import User
from django.test import TestCase
from mock_django import ModelMock

from data_api.models import Hit
from data_api.serializers import HitSerializer

class HitSerializerTestCase(TestCase):

    def setUp(self):
        self.user_instance = ModelMock(User)
        self.user_instance.id = 1

        self.hit = Hit.objects.create(triggered_by="eating", area="VL3",
                                      note="note1",
                                      rank=5, meds=True,
                                      owner=self.user_instance)
        self.hit_serializer = HitSerializer(instance=self.hit)

    def test_serializer_repr(self):
        data = self.hit_serializer.data
        self.assertEqual(set(data.keys()), set(['created', 'id', 'triggered_by',
                                          'area', 'note', 'rank', 'meds',
                                          'owner']))

    def test_serializer_type(self):
        data = self.hit_serializer.data
        self.assertEqual(type(data.serializer), HitSerializer)
