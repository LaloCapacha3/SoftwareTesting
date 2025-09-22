# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from class_exercises import (
    TrafficLight,
    calculate_total_discount,
    check_number_status,
    validate_password,
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_check_number_status_positive(self):
        """
        Checks if a number is positive.
        """
        self.assertEqual(check_number_status(5), "Positive")

    def test_check_number_status_negative(self):
        """
        Checks if a number is negative.
        """
        self.assertEqual(check_number_status(-3), "Negative")

    def test_check_number_status_zero(self):
        """
        Checks if a number is zero.
        """
        self.assertEqual(check_number_status(0), "Zero")

    def test_validate_password_strong(self):
        """
        Checks if a password is strong.
        """
        self.assertTrue(validate_password("StrongPass1!"))

    def test_validate_password_weak_length(self):
        """
        Checks if a password is weak due to length.
        """
        self.assertFalse(validate_password("Short1!"))

    def test_validate_password_weak_no_upper(self):
        """
        Checks if a password is weak due to no uppercase letter.
        """
        self.assertFalse(validate_password("weakpass1!"))

    def test_validate_password_weak_no_digit(self):
        """
        Checks if a password is weak due to no digit.
        """
        self.assertFalse(validate_password("WeakPass!"))

    def test_validate_password_weak_no_special(self):
        """
        Checks if a password is weak due to no special character.
        """
        self.assertFalse(validate_password("WeakPass1"))

    def test_calculate_total_discount_no_discount(self):
        """
        Checks total discount when no discounts apply.
        """
        self.assertEqual(calculate_total_discount(50), 0)

    def test_calculate_total_discount_ten_percent(self):
        """
        Checks total discount when 10% discount applies.
        """
        self.assertEqual(calculate_total_discount(150), 15)

    def test_calculate_total_discount_twenty_percent(self):
        """
        Checks total discount when 20% discount applies.
        """
        self.assertEqual(calculate_total_discount(600), 120)

    def test_traffic_light_initial_state(self):
        """
        Checks the initial state of the traffic light.
        """
        light = TrafficLight()
        self.assertEqual(light.state, "Red")

    def test_traffic_light_next_state(self):
        """
        Checks the state transitions of the traffic light.
        """
        light = TrafficLight()
        light.change_state()
        self.assertEqual(light.state, "Green")
        light.change_state()
        self.assertEqual(light.state, "Yellow")
        light.change_state()
        self.assertEqual(light.state, "Red")
