from django.test import TestCase

from . calc import add, subtract, multiply


class CalcTest(TestCase):
    def test_calc_add(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtract(5, 11), 6)

    def test_cal_multiply(self):
        """Test that values are multiplied and returned"""
        self.assertEqual(multiply(9, 11), 99)
