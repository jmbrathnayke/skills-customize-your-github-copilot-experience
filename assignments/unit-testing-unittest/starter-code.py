import unittest

# Functions to test (students will write tests for these)

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def divide(a, b):
    """Return a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_palindrome(text):
    """Check if a string is a palindrome (ignoring spaces and case)."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def find_max(numbers):
    """Return the maximum number in a list. Raises ValueError if list is empty."""
    if not numbers:
        raise ValueError("Cannot find max of empty list")
    return max(numbers)


# TODO: Write your test cases below

class TestArithmetic(unittest.TestCase):
    """Tests for arithmetic functions."""

    # TODO: Test the add() function with typical values
    # TODO: Test the add() function with negative numbers
    # TODO: Test the add() function with zero

    # TODO: Test divide() with positive numbers
    # TODO: Test divide() with negative numbers
    # TODO: Test that divide() raises ValueError when dividing by zero


class TestStringFunctions(unittest.TestCase):
    """Tests for string manipulation functions."""

    # TODO: Test is_palindrome() with a simple palindrome
    # TODO: Test is_palindrome() with a non-palindrome
    # TODO: Test is_palindrome() with spaces and mixed case
    # TODO: Test is_palindrome() with empty string


class TestListFunctions(unittest.TestCase):
    """Tests for list manipulation functions."""

    # TODO: Test find_max() with positive numbers
    # TODO: Test find_max() with negative numbers
    # TODO: Test find_max() with a single element
    # TODO: Test that find_max() raises ValueError for empty list


if __name__ == "__main__":
    unittest.main()
