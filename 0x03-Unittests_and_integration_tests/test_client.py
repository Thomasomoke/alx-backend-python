#!/usr/bin/env python3

"""
Unit tests for the client module.
Tests GithubOrgClient functionality
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient class.
    Verifies that the org method returns the expected values.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Tests that GithubOrgClient.org returns correct
        organization data.
        """
        mock_get_json.return_value = {"org_name": org_name}
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with
        (f'https://api.github.com/orgs/{org_name}')
        self.assertEqual(result, {"org_name": org_name})


if __name__ == "__main__":
    unittest.main()
