# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from class_exercises import (
    ElevatorSystem,
    UserAuthentication,
    authenticate_user,
    calculate_quantity_discount,
    calculate_shipping_cost,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    get_weather_advisory,
    grade_quiz,
    validate_credit_card,
    validate_date,
    validate_url,
)


# pylint: disable=too-many-public-methods
class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_validate_credit_card_valid(self):
        """
        Validates credit card when it is valid
        """
        credit_card = "1234567890123"
        self.assertEqual(validate_credit_card(credit_card), "Valid Card")

    def test_validate_credit_card_invalid_short(self):
        """
        Tries to validate credit card when it is invalid because it's too short
        """
        credit_card = "123456789012"
        self.assertEqual(validate_credit_card(credit_card), "Invalid Card")

    def test_validate_credit_card_invalid_long(self):
        """
        Tries to validate credit card when it is invalid because it's too long
        """
        credit_card = "12345678901234567"
        self.assertEqual(validate_credit_card(credit_card), "Invalid Card")

    def test_validate_credit_card_no_digits(self):
        """
        Tries to validate credit card when it is invalid because it has no digits
        """
        credit_card = "abcdefghijklmnopqrstuv"
        self.assertEqual(validate_credit_card(credit_card), "Invalid Card")

    def test_validate_date(self):
        """
        Validates date
        """
        year = 2025
        month = 10
        day = 6
        self.assertEqual(validate_date(year, month, day), "Valid Date")

    def test_validate_date_invalid_year(self):
        """
        Tries to validates date when the year is invalid
        """
        year = 2101
        month = 10
        day = 6
        self.assertEqual(validate_date(year, month, day), "Invalid Date")

    def test_validate_date_invalid_month(self):
        """
        Tries to validates date when the month is invalid
        """
        year = 2025
        month = 13
        day = 6
        self.assertEqual(validate_date(year, month, day), "Invalid Date")

    def test_validate_date_invalid_day(self):
        """
        Tries to validates date when the day is invalid
        """
        year = 2025
        month = 10
        day = 32
        self.assertEqual(validate_date(year, month, day), "Invalid Date")

    def test_check_flight_eligibility(self):
        """
        Validates flight elegibility
        """
        age = 20
        frequent_flyer = False
        self.assertEqual(
            check_flight_eligibility(age, frequent_flyer), "Eligible to Book"
        )

    def test_check_flight_eligibility_frequent_flyer(self):
        """
        Validates flight elegibility when the user is a frequent flyer
        """
        age = 17
        frequent_flyer = True
        self.assertEqual(
            check_flight_eligibility(age, frequent_flyer), "Eligible to Book"
        )

    def test_check_flight_eligibility_not_eligible(self):
        """
        Tries to validate flight elegibility when the user is not eligible
        """
        age = 17
        frequent_flyer = False
        self.assertEqual(
            check_flight_eligibility(age, frequent_flyer), "Not Eligible to Book"
        )

    def test_validate_url_valid_http(self):
        """
        Validates URL when it is valid and starts with http
        """
        url = "http://example.com"
        self.assertEqual(validate_url(url), "Valid URL")

    def test_validate_url_valid_https(self):
        """
        Validates URL when it is valid and starts with https
        """
        url = "https://example.com"
        self.assertEqual(validate_url(url), "Valid URL")

    def test_validate_url_invalid_too_long(self):
        """
        Tries to validate URL when it is invalid because it's too long
        """
        url = "http://" + "a" * 250 + ".com"
        self.assertEqual(validate_url(url), "Invalid URL")

    def test_validate_url_invalid_no_http(self):
        """
        Tries to validate URL when it is invalid because it doesn't start with http or https
        """
        url = "ftp://example.com"
        self.assertEqual(validate_url(url), "Invalid URL")

    def test_calculate_quantity_discount_no_discount(self):
        """
        Calculates quantity discount when there is no discount
        """
        quantity = 3
        self.assertEqual(calculate_quantity_discount(quantity), "No Discount")

    def test_calculate_quantity_discount_5_percent(self):
        """
        Calculates quantity discount when there is a 5% discount
        """
        quantity = 7
        self.assertEqual(calculate_quantity_discount(quantity), "5% Discount")

    def test_calculate_quantity_discount_10_percent(self):
        """
        Calculates quantity discount when there is a 10% discount
        """
        quantity = 15
        self.assertEqual(calculate_quantity_discount(quantity), "10% Discount")

    def test_check_file_size_valid(self):
        """
        Checks file size when it is valid
        """
        size_in_bytes = 500000
        self.assertEqual(check_file_size(size_in_bytes), "Valid File Size")

    def test_check_file_size_invalid_negative(self):
        """
        Tries to check file size when it is invalid because it's negative
        """
        size_in_bytes = -100
        self.assertEqual(check_file_size(size_in_bytes), "Invalid File Size")

    def test_check_file_size_invalid_too_large(self):
        """
        Tries to check file size when it is invalid because it's too large
        """
        size_in_bytes = 2000000
        self.assertEqual(check_file_size(size_in_bytes), "Invalid File Size")

    def test_check_loan_eligibility_not_eligible(self):
        """
        Checks loan eligibility when the user is not eligible
        """
        income = 25000
        credit_score = 650
        self.assertEqual(check_loan_eligibility(income, credit_score), "Not Eligible")

    def test_check_loan_eligibility_secured_loan(self):
        """
        Checks loan eligibility when the user is eligible for a secured loan
        """
        income = 40000
        credit_score = 650
        self.assertEqual(check_loan_eligibility(income, credit_score), "Secured Loan")

    def test_check_loan_eligibility_standard_loan(self):
        """
        Checks loan eligibility when the user is eligible for a standard loan
        """
        income = 40000
        credit_score = 720
        self.assertEqual(check_loan_eligibility(income, credit_score), "Standard Loan")

    def test_check_loan_eligibility_premium_loan(self):
        """
        Checks loan eligibility when the user is eligible for a premium loan
        """
        income = 70000
        credit_score = 800
        self.assertEqual(check_loan_eligibility(income, credit_score), "Premium Loan")

    def test_check_loan_eligibility_standard_loan_high_income(self):
        """
        Checks loan eligibility when the user is eligible for a standard loan with high income
        """
        income = 70000
        credit_score = 700
        self.assertEqual(check_loan_eligibility(income, credit_score), "Standard Loan")

    def test_calculate_shipping_cost_5(self):
        """
        Calculates shipping cost when it is $5
        """
        weight = 0.5
        length = 5
        width = 5
        height = 5
        self.assertEqual(calculate_shipping_cost(weight, length, width, height), 5)

    def test_calculate_shipping_cost_10(self):
        """
        Calculates shipping cost when it is $10
        """
        weight = 3
        length = 20
        width = 20
        height = 20
        self.assertEqual(calculate_shipping_cost(weight, length, width, height), 10)

    def test_calculate_shipping_cost_20(self):
        """
        Calculates shipping cost when it is $20
        """
        weight = 10
        length = 40
        width = 40
        height = 40
        self.assertEqual(calculate_shipping_cost(weight, length, width, height), 20)

    def test_grade_quiz_pass(self):
        """
        Grades quiz when the user passes
        """
        correct_answers = 8
        incorrect_answers = 1
        self.assertEqual(grade_quiz(correct_answers, incorrect_answers), "Pass")

    def test_grade_quiz_conditional_pass(self):
        """
        Grades quiz when the user gets a conditional pass
        """
        correct_answers = 6
        incorrect_answers = 2
        self.assertEqual(
            grade_quiz(correct_answers, incorrect_answers), "Conditional Pass"
        )

    def test_grade_quiz_fail(self):
        """
        Grades quiz when the user fails
        """
        correct_answers = 4
        incorrect_answers = 4
        self.assertEqual(grade_quiz(correct_answers, incorrect_answers), "Fail")

    def test_authenticate_user_admin(self):
        """
        Authenticates user when they are an admin
        """
        username = "admin"
        password = "admin123"
        self.assertEqual(authenticate_user(username, password), "Admin")

    def test_authenticate_user_user(self):
        """
        Authenticates user when they are a regular user
        """
        username = "user123"
        password = "password123"
        self.assertEqual(authenticate_user(username, password), "User")

    def test_authenticate_user_invalid(self):
        """
        Tries to authenticate user when they are invalid
        """
        username = "usr"
        password = "pwd"
        self.assertEqual(authenticate_user(username, password), "Invalid")

    def test_get_weather_advisory_humid_and_hot(self):
        """
        Gets weather advisory when it is humid and hot
        """
        temperature = 35
        humidity = 80
        self.assertEqual(
            get_weather_advisory(temperature, humidity),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_get_weather_advisory_cold(self):
        """
        Gets weather advisory when it is cold
        """
        temperature = -5
        humidity = 50
        self.assertEqual(
            get_weather_advisory(temperature, humidity), "Low Temperature. Bundle Up!"
        )

    def test_get_weather_advisory_no_advisory(self):
        """
        Gets weather advisory when there is no specific advisory
        """
        temperature = 20
        humidity = 50
        self.assertEqual(
            get_weather_advisory(temperature, humidity), "No Specific Advisory"
        )

    def test_user_authentication_login_logout(self):
        """
        Tests the UserAuthentication class for login and logout functionality.
        """
        auth_system = UserAuthentication()

        # Initial state should be "Logged Out"
        self.assertEqual(auth_system.state, "Logged Out")

        # Test login
        login_result = auth_system.login()
        self.assertEqual(login_result, "Login successful")
        self.assertEqual(auth_system.state, "Logged In")

        # Test invalid login when already logged in
        invalid_login_result = auth_system.login()
        self.assertEqual(invalid_login_result, "Invalid operation in current state")
        self.assertEqual(auth_system.state, "Logged In")

        # Test logout
        logout_result = auth_system.logout()
        self.assertEqual(logout_result, "Logout successful")
        self.assertEqual(auth_system.state, "Logged Out")

        # Test invalid logout when already logged out
        invalid_logout_result = auth_system.logout()
        self.assertEqual(invalid_logout_result, "Invalid operation in current state")
        self.assertEqual(auth_system.state, "Logged Out")

    def test_elevator_system_movement(self):
        """
        Tests the ElevatorSystem class for movement functionality.
        """
        elevator = ElevatorSystem()

        # Initial state should be "Idle"
        self.assertEqual(elevator.state, "Idle")

        # Test move up
        move_up_result = elevator.move_up()
        self.assertEqual(move_up_result, "Elevator moving up")
        self.assertEqual(elevator.state, "Moving Up")

        # Test invalid move up when already moving
        invalid_move_up_result = elevator.move_up()
        self.assertEqual(invalid_move_up_result, "Invalid operation in current state")
        self.assertEqual(elevator.state, "Moving Up")

        # Test stop
        stop_result = elevator.stop()
        self.assertEqual(stop_result, "Elevator stopped")
        self.assertEqual(elevator.state, "Idle")

        # Test move down
        move_down_result = elevator.move_down()
        self.assertEqual(move_down_result, "Elevator moving down")
        self.assertEqual(elevator.state, "Moving Down")

        # Test invalid move down when already moving
        invalid_move_down_result = elevator.move_down()
        self.assertEqual(invalid_move_down_result, "Invalid operation in current state")
        self.assertEqual(elevator.state, "Moving Down")

        # Test stop again
        stop_result_again = elevator.stop()
        self.assertEqual(stop_result_again, "Elevator stopped")
        self.assertEqual(elevator.state, "Idle")
