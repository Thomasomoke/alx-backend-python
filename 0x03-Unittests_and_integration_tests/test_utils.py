#!/usr/bin/env python3


import unittest
from parameterized import parameterized
from utils import access_nested_map
"""
importing relevant modules
and files
"""


class TestAccessNestedMap(unittest.TestCase):
    """Test suite for access_nested_map function.
    Verifies correct value retrieval from nested dictionaries.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests access_nested_map with given path.
        Confirms it returns the expected value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'"),
    ])
    def test_access_nested_map_exception
    (self, nested_map, path, expected_message):
        """Tests access_nested_map raises KeyError for invalid path.
        Checks if the error message matches the expected output.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
