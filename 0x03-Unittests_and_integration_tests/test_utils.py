#!/usr/bin/env python3

"""
Unit tests for the utils module.
Tests memoization of methods to ensure efficient calls.
"""

import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Test suite for memoize decorator.
    Verifies that decorated methods cache results correctly.
    """

    @patch('utils.TestClass.a_method')
    def test_memoize(self, mock_a_method):
        """Tests that memoization works as expected.
        Ensures a method is called only once when memoized.
        """

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        mock_a_method.return_value = 42
        test_instance = TestClass()
        first_call = test_instance.a_property()
        second_call = test_instance.a_property()
        self.assertEqual(first_call, second_call)
        mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
