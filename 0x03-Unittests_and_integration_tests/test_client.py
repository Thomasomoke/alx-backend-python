#!/usr/bin/env python3

"""
Unit tests for the client module.
Tests GithubOrgClient functionality, focusing on public repositories.
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient class."""

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Tests that public_repos returns the expected
        list of repositories."""
        mock_get_json.return_value = [
            {"name": "repo1", "url":
                "https://api.github.com/repos/example/repo1"},
            {"name": "repo2", "url":
                "https://api.github.com/repos/example/repo2"},
        ]

        with patch
        ('client.GithubOrgClient._public_repos_url', new_callable=property)
        as mock_public_repos_url:
            mock_public_repos_url.return_value =
            "https://api.github.com/orgs/example/repos"
            client = GithubOrgClient("example")
            repos = client.public_repos()
            expected_repos = ["repo1", "repo2"]
            self.assertEqual(repos, expected_repos)
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with
            ("https://api.github.com/orgs/example/repos")


if __name__ == "__main__":
    unittest.main()
