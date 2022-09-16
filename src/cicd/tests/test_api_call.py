from django.test import TestCase


class TestGetTokens(TestCase):

    def setUp(self):
        from cicd.models import Repo, GithubToken
        github_token = GithubToken.objects.create(name="test_token", token="NOT_VALID_TOKEN")
        Repo.objects.create(owner="amirmahdy", repository="market_data_provider")
        Repo.objects.create(owner="amirmahdy", repository="order_bird", token=github_token)

    def test_call_api_public(self):
        """
        This test checks if using the above token we can get a result from call_api method
        This repository is public and does not require a token
        """
        from cicd.github import GithubRepoClass
        github = GithubRepoClass('amirmahdy', 'market_data_provider')
        validity, result = github.call_api()
        self.assertEqual(result.status_code, 200)

    def test_call_api_not_existent(self):
        """
        This test checks if using the above token we can get a result from call_api method
        This repository does not exists.
        """
        from cicd.github import GithubRepoClass
        github = GithubRepoClass('amirmahdy', 'order_bird')
        validity, result = github.call_api()
        self.assertEqual(validity, False)

    def test_call_api_private(self):
        """
        This test checks if using the above token we can get a result from call_api method
        This repository is private.
        """
        from cicd.github import GithubRepoClass
        github = GithubRepoClass('amirmahdy', 'crypto')
        validity, result = github.call_api()
        self.assertEqual(validity, False)