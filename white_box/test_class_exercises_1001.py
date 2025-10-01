# -*- coding: utf-8 -*-

"""
Mock up testing examples.
"""
import unittest
from unittest.mock import patch

from white_box.class_exercises import BankAccount, BankingSystem, Product, ShoppingCart


class TestBank(unittest.TestCase):
    """
    Bank unittest class.
    """

    def setUp(self):
        """
        Set up the BankingSystem instance before each test.
        """
        self.banking_system = BankingSystem()
        self.banking_system.authenticate("user123", "pass123")

    def test_successful_transfer(self):
        """
        Test a successful money transfer.
        """
        result = self.banking_system.transfer_money(
            "user123", "receiver456", 100, "regular"
        )
        self.assertTrue(result)

    def test_insufficient_funds(self):
        """
        Test a money transfer with insufficient funds.
        """
        result = self.banking_system.transfer_money(
            "user123", "receiver456", 2000, "regular"
        )
        self.assertFalse(result)

    def test_invalid_transaction_type(self):
        """
        Test a money transfer with an invalid transaction type.
        """
        result = self.banking_system.transfer_money(
            "user123", "receiver456", 100, "invalid_type"
        )
        self.assertFalse(result)

    def test_unauthenticated_sender(self):
        """
        Test a money transfer with an unauthenticated sender.
        """
        result = self.banking_system.transfer_money(
            "unknown_user", "receiver456", 100, "regular"
        )
        self.assertFalse(result)

    def test_view_account(self):
        """
        Test viewing account details.
        """
        account = BankAccount("user123", 500)
        with patch("builtins.print") as mock_print:
            account.view_account()
            mock_print.assert_called_with("The account user123 has a balance of 500")


class TestShoppingCart(unittest.TestCase):
    """
    Shopping cart unittest class.
    """

    def setUp(self):
        """
        Set up the ShoppingCart instance before each test.
        """
        self.cart = ShoppingCart()
        self.product1 = Product("Laptop", 1000)
        self.product2 = Product("Phone", 500)

    def test_add_product(self):
        """
        Test adding products to the shopping cart.
        """
        self.cart.add_product(self.product1, 2)
        self.cart.add_product(self.product2, 1)
        self.assertEqual(len(self.cart.items), 2)
        self.assertEqual(self.cart.items[0]["quantity"], 2)
        self.assertEqual(self.cart.items[1]["quantity"], 1)

    def test_remove_product(self):
        """
        Test removing products from the shopping cart.
        """
        self.cart.add_product(self.product1, 2)
        self.cart.remove_product(self.product1, 1)
        self.assertEqual(self.cart.items[0]["quantity"], 1)
        self.cart.remove_product(self.product1, 1)
        self.assertEqual(len(self.cart.items), 0)

    def test_view_cart(self):
        """
        Test viewing the shopping cart content.
        """
        self.cart.add_product(self.product1, 1)
        self.cart.add_product(self.product2, 2)
        with patch("builtins.print") as mock_print:
            self.cart.view_cart()
            mock_print.assert_any_call("1 x Laptop - $1000")
            mock_print.assert_any_call("2 x Phone - $1000")

    def test_checkout(self):
        """
        Test checking out the shopping cart.
        """
        self.cart.add_product(self.product1, 1)
        self.cart.add_product(self.product2, 2)
        with patch("builtins.print") as mock_print:
            self.cart.checkout()
            mock_print.assert_any_call("Total: $2000")
            mock_print.assert_any_call("Checkout completed. Thank you for shopping!")

    def test_view_product(self):
        """
        Test viewing product details.
        """
        with patch("builtins.print") as mock_print:
            msg = self.product1.view_product()
            mock_print.assert_called_with("The product Laptop has a price of 1000")
            self.assertEqual(msg, "The product Laptop has a price of 1000")
