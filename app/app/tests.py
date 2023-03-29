from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    "Test the calc"

    def test_add_number(self):
        res = calc.add(3,4)
        self.assertEqual(res,7)
