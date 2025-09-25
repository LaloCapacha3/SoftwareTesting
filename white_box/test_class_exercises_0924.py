# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from class_exercises import (
    calculate_items_shipping_cost,
    calculate_order_total,
    categorize_product,
    celsius_to_fahrenheit,
    validate_email,
    validate_login,
    verify_age,
)


# pylint: disable=too-many-public-methods
class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_calculate_order_total_no_discount(self):
        """
        Checks total price when no discount applies (1-5 items).
        """
        items = [{"quantity": 3, "price": 100}]
        self.assertEqual(calculate_order_total(items), 300)

    def test_calculate_order_total_5_percent_discount(self):
        """
        Checks total price when 5% discount applies (6-10 items).
        """
        items = [{"quantity": 6, "price": 50}]
        self.assertAlmostEqual(calculate_order_total(items), 285, places=2)

    def test_calculate_order_total_10_percent_discount(self):
        """
        Checks total price when 10% discount applies (more than 10 items).
        """
        items = [{"quantity": 15, "price": 20}]
        self.assertEqual(calculate_order_total(items), 270)

    def test_calculate_order_total_mixed_items(self):
        """
        Checks total price when the order has items with different discount ranges.
        """
        items = [
            {"quantity": 2, "price": 100},
            {"quantity": 7, "price": 50},
            {"quantity": 12, "price": 10},
        ]
        self.assertEqual(calculate_order_total(items), 200 + 332.5 + 108)

    def test_calculate_items_shipping_cost_standard_low_weight(self):
        """
        Checks shipping cost for standard shipping with total weight <= 5.
        """
        items = [{"weight": 2}, {"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_calculate_items_shipping_cost_standard_medium_weight(self):
        """
        Checks shipping cost for standard shipping with total weight between 5 and 10.
        """
        items = [{"weight": 4}, {"weight": 4}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_calculate_items_shipping_cost_standard_high_weight(self):
        """
        Checks shipping cost for standard shipping with total weight > 10.
        """
        items = [{"weight": 6}, {"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_calculate_items_shipping_cost_express_low_weight(self):
        """
        Checks shipping cost for express shipping with total weight <= 5.
        """
        items = [{"weight": 1}, {"weight": 4}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_calculate_items_shipping_cost_express_medium_weight(self):
        """
        Checks shipping cost for express shipping with total weight between 5 and 10.
        """
        items = [{"weight": 3}, {"weight": 4}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_calculate_items_shipping_cost_express_high_weight(self):
        """
        Checks shipping cost for express shipping with total weight > 10.
        """
        items = [{"weight": 7}, {"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_calculate_items_shipping_cost_invalid_method(self):
        """
        Checks that a ValueError is raised for an invalid shipping method.
        """
        items = [{"weight": 2}, {"weight": 3}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "overnight")

    def test_validate_login_successful(self):
        """
        Checks login validation for valid username and password lengths.
        """
        self.assertEqual(validate_login("validUser", "strongPass1"), "Login Successful")

    def test_validate_login_failed(self):
        """
        Checks login validation for invalid username and password lengths.
        """
        self.assertEqual(validate_login("usr", "pwd"), "Login Failed")
        self.assertEqual(
            validate_login("thisusernameiswaytoolongtobevalid", "strongPass1"),
            "Login Failed",
        )
        self.assertEqual(validate_login("validUser", "short"), "Login Failed")
        self.assertEqual(
            validate_login("validUser", "thispasswordiswaytoolongtobevalid"),
            "Login Failed",
        )

    def test_verify_age_eligible(self):
        """
        Checks age verification for eligible ages.
        """
        self.assertEqual(verify_age(18), "Eligible")
        self.assertEqual(verify_age(30), "Eligible")
        self.assertEqual(verify_age(65), "Eligible")

    def test_verify_age_not_eligible(self):
        """
        Checks age verification for non-eligible ages.
        """
        self.assertEqual(verify_age(17), "Not Eligible")
        self.assertEqual(verify_age(66), "Not Eligible")
        self.assertEqual(verify_age(-5), "Not Eligible")
        self.assertEqual(verify_age(100), "Not Eligible")

    def test_categorize_product(self):
        """
        Checks product categorization based on price ranges.
        """
        self.assertEqual(categorize_product(10), "Category A")
        self.assertEqual(categorize_product(50), "Category A")
        self.assertEqual(categorize_product(51), "Category B")
        self.assertEqual(categorize_product(100), "Category B")
        self.assertEqual(categorize_product(101), "Category C")
        self.assertEqual(categorize_product(200), "Category C")
        self.assertEqual(categorize_product(5), "Category D")
        self.assertEqual(categorize_product(250), "Category D")

    def test_validate_email_valid(self):
        """
        Checks email validation for correctly formatted valid emails.
        """
        self.assertEqual(validate_email("user@example.com"), "Valid Email")
        self.assertEqual(validate_email("abc.def@domain.org"), "Valid Email")
        self.assertEqual(validate_email("a_b-c123@sub.domain.co"), "Valid Email")
        self.assertEqual(validate_email("a" * 38 + "@example.com"), "Valid Email")

    def test_validate_email_invalid_too_short(self):
        """
        Checks email validation for emails shorter than 5 characters.
        """
        self.assertEqual(validate_email("a@b"), "Invalid Email")

    def test_validate_email_invalid_too_long(self):
        """
        Checks email validation for emails longer than 50 characters.
        """
        self.assertEqual(
            validate_email("a" * 45 + "@exampletoolongdomain.com"), "Invalid Email"
        )

    def test_validate_email_missing_at_symbol(self):
        """
        Checks email validation when '@' is missing.
        """
        self.assertEqual(validate_email("userexample.com"), "Invalid Email")

    def test_validate_email_missing_dot(self):
        """
        Checks email validation when '.' is missing.
        """
        self.assertEqual(validate_email("user@examplecom"), "Invalid Email")

    def test_validate_email_empty_string(self):
        """
        Checks email validation for an empty string.
        """
        self.assertEqual(validate_email(""), "Invalid Email")

    def test_celsius_to_fahrenheit_valid(self):
        """
        Checks temperature conversion for valid Celsius values.
        """
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40)
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6)

    def test_celsius_to_fahrenheit_invalid(self):
        """
        Checks temperature conversion for invalid Celsius values.
        """
        self.assertEqual(celsius_to_fahrenheit(-150), "Invalid Temperature")
        self.assertEqual(celsius_to_fahrenheit(150), "Invalid Temperature")
