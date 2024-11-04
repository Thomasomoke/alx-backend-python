#!/usr/bin/env python3

"""
Integration tests for GithubOrgClient.
Testing GithubOrgClient.public_repos method with fixture data.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload,
expected_repos, apache2_repos


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload,
     "expected_repos": expected_repos, "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test suite for GithubOrgClient with fixture data."""

    @classmethod
    def setUpClass(cls):
        """Sets up the mock for requests.get using the fixtures."""
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        def get_json_side_effect(url):
            if url == f"https://api.github.com/orgs/{org_payload['login']}":
                return org_payload
            elif url == org_payload['repos_url']:
                return repos_payload
            return None

        mock_get.return_value.json.side_effect = get_json_side_effect

    @classmethod
    def tearDownClass(cls):
        """Stops the requests.get patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Tests that public_repos returns expected repository names."""
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Tests that public_repos returns only
        repos with specified license."""
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual
        (client.public_repos(license="apache-2.0"), self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
