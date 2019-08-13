from django.contrib.auth.models import User
from django.test import TestCase
from mock_django import ModelMock

from data_api.models import Hit


class HiTest(TestCase):
    """ Tests module for Hit model """
    def setUp(self):
        self.user_instance = ModelMock(User)
        self.user_instance.id = 1
        self.hit = Hit.objects.create(triggered_by="eating", area="VL3",
                                 note="note1",
                                 rank=5, meds=True, owner=self.user_instance)

        self.hit.save()

    def test_hit_identity(self):
        self.assertIsInstance(self.hit, Hit)

    def test_count(self):
        self.assertEqual(Hit.objects.count(), 1)

    def test_hit_list(self):
        self.assertEqual(1, len(Hit.objects.all()))

    def test_hit_repr(self):
        self.assertIn("had a pain ranked with 5 on area VL3 triggered by "
                      "eating at", self.hit.__str__())

    def test_hit_delete(self):
        self.hit.delete()
        self.assertEqual(0, Hit.objects.count())