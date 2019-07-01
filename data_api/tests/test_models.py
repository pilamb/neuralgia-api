from django.contrib.auth.models import User
from django.test import TestCase
from mock_django import ModelMock

from data_api.models import Hit


class HiTest(TestCase):
    """ Tests module for Hit model """
    def setUp(self):
        self.user_instance = ModelMock(User)
        self.user_instance.id = 1

    def test_hit_create(self):
        hit = Hit.objects.create(triggered_by="eating", area="VL3", note="note1",
                           rank=5, meds=True, owner=self.user_instance)
        self.assertIsInstance(self.user_instance, User)
        self.assertIsInstance(hit, Hit)
        self.assertEqual(Hit.objects.count(), 1)
