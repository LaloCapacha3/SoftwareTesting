# -*- coding: utf-8 -*-

"""
Mock up testing examples.
"""
import subprocess
import unittest
from unittest.mock import patch

import requests

from white_box.mockup_exercises import (
    execute_command,
    fetch_data_from_api,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestDataFetcher(unittest.TestCase):
    """
    Data fetcher unittest class.
    """

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Success case.
        """
        # Set up the mock response
        mock_get.return_value.json.return_value = {"key": "value"}

        # Mock the requests.get method
        # with patch("requests.get") as mock_get:
        #     mock_get.return_value.status_code = 200
        #     mock_get.return_value.json.return_value = [
        #         {"id": 1, "title": "Title 1", "body": "Body 1"},
        #         {"id": 2, "title": "Title 2", "body": "Body 2"},
        #     ]

        # mock_get = patch('requests.get')
        # mock_get.return_value.status_code = 200
        # mock_get.return_value.json.return_value = [
        #     {"id": 1, "title": "Title 1", "body": "Body 1"},
        #     {"id": 2, "title": "Title 2", "body": "Body 2"},
        # ]

        # Call the function under test
        result = fetch_data_from_api("https://api.example.com/data")

        # Assert that the function returns the expected result
        self.assertEqual(result, {"key": "value"})

        # Assert that requests.get was called with the correct URL
        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)

    def test_fetch_data_from_api_failure(self):
        """
        Failure case.
        """
        # Mock the requests.get method to raise an exception
        with patch("white_box.mockup_exercises.requests.get") as mock_get:
            mock_get.side_effect = Exception("API request failed")

            # Call the function under test and assert that it raises an exception
            with self.assertRaises(Exception) as context:
                fetch_data_from_api("https://api.example.com/data")

            self.assertEqual(str(context.exception), "API request failed")

            # Assert that requests.get was called with the correct URL
            mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)

    def test_fetch_data_from_api_timeout(self):
        """
        Timeout case.
        """
        # Mock the requests.get method to raise a timeout exception
        with patch("white_box.mockup_exercises.requests.get") as mock_get:
            mock_get.side_effect = requests.Timeout("Request timed out")

            # Call the function under test and assert that it raises a timeout exception
            with self.assertRaises(requests.Timeout) as context:
                fetch_data_from_api("https://api.example.com/data")

            self.assertEqual(str(context.exception), "Request timed out")

            # Assert that requests.get was called with the correct URL
            mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)


class TestFileReader(unittest.TestCase):
    """
    File reader unittest class.
    """

    def test_read_data_from_file_success(self):
        """
        Success case.
        """
        # Mock the open function to simulate reading from a file
        mock_open = patch(
            "builtins.open", unittest.mock.mock_open(read_data="file content")
        ).start()

        # Call the function under test
        result = read_data_from_file("testfile.txt")

        # Assert that the function returns the expected result
        self.assertEqual(result, "file content")

        # Assert that open was called with the correct filename and encoding
        mock_open.assert_called_once_with("testfile.txt", encoding="utf-8")

        # Stop the patcher
        patch.stopall()

    def test_read_data_from_file_not_found(self):
        """
        File not found case.
        """
        # Mock the open function to raise a FileNotFoundError
        with patch(
            "builtins.open", side_effect=FileNotFoundError("File not found")
        ) as mock_open:
            # Call the function under test and assert that it raises a FileNotFoundError
            with self.assertRaises(FileNotFoundError) as context:
                read_data_from_file("nonexistentfile.txt")

            self.assertEqual(str(context.exception), "File not found")

            # Assert that open was called with the correct filename and encoding
            mock_open.assert_called_once_with("nonexistentfile.txt", encoding="utf-8")


class TestCommandExecutor(unittest.TestCase):
    """
    Command executor unittest class.
    """

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_success(self, mock_run):
        """
        Success case.
        """
        # Set up the mock subprocess.run return value
        mock_run.return_value.stdout = "command output"

        # Call the function under test
        result = execute_command(["echo", "Hello, World!"])

        # Assert that the function returns the expected result
        self.assertEqual(result, "command output")

        # Assert that subprocess.run was called with the correct command and parameters
        mock_run.assert_called_once_with(
            ["echo", "Hello, World!"],
            capture_output=True,
            check=False,
            text=True,
        )

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_failure(self, mock_run):
        """
        Failure case.
        """
        # Set up the mock subprocess.run to raise a CalledProcessError
        mock_run.side_effect = subprocess.CalledProcessError(
            returncode=1, cmd=["false"]
        )

        # Call the function under test and assert that it raises a CalledProcessError
        with self.assertRaises(subprocess.CalledProcessError) as context:
            execute_command(["false"])

        self.assertEqual(context.exception.returncode, 1)
        self.assertEqual(context.exception.cmd, ["false"])

        # Assert that subprocess.run was called with the correct command and parameters
        mock_run.assert_called_once_with(
            ["false"],
            capture_output=True,
            check=False,
            text=True,
        )


class TestTimeBasedAction(unittest.TestCase):
    """
    Time-based action unittest class.
    """

    @patch("white_box.mockup_exercises.time.time", return_value=5)
    def test_perform_action_based_on_time_action_a(self, mock_time):
        """
        Action A case.
        """
        # Call the function under test
        result = perform_action_based_on_time()

        # Assert that the function returns the expected result
        self.assertEqual(result, "Action A")

        # Assert that time.time was called once
        mock_time.assert_called_once()

    @patch("white_box.mockup_exercises.time.time", return_value=15)
    def test_perform_action_based_on_time_action_b(self, mock_time):
        """
        Action B case.
        """
        # Call the function under test
        result = perform_action_based_on_time()

        # Assert that the function returns the expected result
        self.assertEqual(result, "Action B")

        # Assert that time.time was called once
        mock_time.assert_called_once()


# class TestPrint(unittest.TestCase):
#     """
#     fetch_data_from_api unittest class.
#     """
#
#     def test_print(self):
#         # Mock the requests.get method
#         mock_print = patch('__main__.print')
#
#         print_hello_world()
#
#         # Verify data is what we expect
#         mock_print.assert_called_once_with("Hello, World!")
