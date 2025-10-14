# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import sys
import unittest
from io import StringIO

from book_store import Book, BookStore


class TestBookStore(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_display_books_empty(self):
        """
        Checks display_books with no books.
        """
        bookstore = BookStore()
        self.assertEqual(len(bookstore.books), 0)
        # Capture the output

        captured_output = StringIO()
        sys.stdout = captured_output
        bookstore.display_books()
        sys.stdout = sys.__stdout__
        self.assertIn("No books in the store.", captured_output.getvalue())

    def test_display_books_with_books(self):
        """
        Checks display_books with some books.
        """
        bookstore = BookStore()
        book1 = Book("Book One", "Author A", 10.99, 5)
        book2 = Book("Book Two", "Author B", 15.99, 3)
        bookstore.add_book(book1)
        bookstore.add_book(book2)
        self.assertEqual(len(bookstore.books), 2)
        # Capture the output

        captured_output = StringIO()
        sys.stdout = captured_output
        bookstore.display_books()
        sys.stdout = sys.__stdout__
        self.assertIn("Books available in the store:", captured_output.getvalue())
        self.assertIn("Title: Book One", captured_output.getvalue())
        self.assertIn("Title: Book Two", captured_output.getvalue())

    def test_search_book_found(self):
        """
        Checks search_book when the book is found.
        """
        bookstore = BookStore()
        book1 = Book("Book One", "Author A", 10.99, 5)
        bookstore.add_book(book1)
        # Capture the output

        captured_output = StringIO()
        sys.stdout = captured_output
        bookstore.search_book("Book One")
        sys.stdout = sys.__stdout__
        self.assertIn(
            "Found 1 book(s) with title 'Book One':", captured_output.getvalue()
        )
        self.assertIn("Title: Book One", captured_output.getvalue())

    def test_search_book_not_found(self):
        """
        Checks search_book when the book is not found.
        """
        bookstore = BookStore()
        book1 = Book("Book One", "Author A", 10.99, 5)
        bookstore.add_book(book1)
        # Capture the output

        captured_output = StringIO()
        sys.stdout = captured_output
        bookstore.search_book("Nonexistent Book")
        sys.stdout = sys.__stdout__
        self.assertIn(
            "No book found with title 'Nonexistent Book'.", captured_output.getvalue()
        )

    def test_add_book(self):
        """
        Checks add_book functionality.
        """
        bookstore = BookStore()
        book1 = Book("Book One", "Author A", 10.99, 5)
        bookstore.add_book(book1)
        self.assertEqual(len(bookstore.books), 1)
        self.assertEqual(bookstore.books[0].title, "Book One")
        self.assertEqual(bookstore.books[0].author, "Author A")
        self.assertEqual(bookstore.books[0].price, 10.99)
        self.assertEqual(bookstore.books[0].quantity, 5)
