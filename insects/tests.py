from django.test import TestCase
from django.contrib.auth.models import User

from .models import Insect


class Insectests(TestCase):
    @classmethod
    def setUpTestData(cls):
        tester = User.objects.create_user(username="tester", password="password")
        tester.save()

        test_insect = Insect.objects.create(
            author  = tester, name="Beetle", can_fly= False, number_of_legs = 6, description = 'Meh'
        )
        test_insect.save()

    def test_insect_content(self):
        insect = Insect.objects.get(id=1)
        expected_author = f"{insect.author}"
        expected_name = f"{insect.name}"
        expected_can_fly = f"{insect.can_fly}"
        expected_number_of_legs = f"{insect.number_of_legs}"
        expected_description = f"{insect.description}"
        self.assertEqual(expected_author, "tester")
        self.assertEqual(expected_name, "Beetle")
        self.assertEqual(expected_can_fly, 'False')
        self.assertEqual(expected_number_of_legs, '6')
        self.assertEqual(expected_description, 'Meh')

