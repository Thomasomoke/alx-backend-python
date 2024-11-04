#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map
"""
import relevant modules for this
project
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


if __name__ == "__main__":
    unittest.main()
