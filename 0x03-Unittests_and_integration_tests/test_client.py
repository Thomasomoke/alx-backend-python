#!/usr/bin/env python3

"""
Unit tests for the client module.
Tests GithubOrgClient functionality
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient class.
    Verifies that the _public_repos_url method returns the expected URL.
    """
    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """Tests that _public_repos_url returns the
        expected URL based on the mocked org.
        """
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/example/repos"
            }
        client = GithubOrgClient("example")
        result = client._public_repos_url()

        self.assertEqual(result, "https://api.github.com/orgs/example/repos")
        mock_org.assert_called_once()


if __name__ == "__main__":
    unittest.main()
