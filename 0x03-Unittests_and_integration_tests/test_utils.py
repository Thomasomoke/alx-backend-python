#!/usr/bin/env python3

"""
Unit tests for the utils module.
Tests get_json
"""

import unittest
from unittest.mock import patch, Mock
from utils import get_json
from parameterized import parameterized


class TestGetJson(unittest.TestCase):
    """Test suite for get_json function.
    Verifies the function correctly retrieves JSON data from a URL.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Tests get_json returns expected payload.
        Confirms the mocked requests.get is called with the correct URL.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
