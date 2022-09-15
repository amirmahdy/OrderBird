from django.test import TestCase


class TestGetTokens(TestCase):

    def setUp(self):
        from cicd.models import Repo, GithubToken
        github_token = GithubToken.objects.create(name="test_token", token="NOT_VALID_TOKEN")
        Repo.objects.create(owner="amirmahdy", repository="market_data_provider")
        Repo.objects.create(owner="amirmahdy", repository="order_bird", token=github_token)

    def test_get_tokens(self):
        """
        This test checks if the above token is accessible via get_token method.
        The test case token will be flushed after test.
        """
        from cicd.github import GithubRepos
        github = GithubRepos('amirmahdy', 'order_bird')
        result = github.get_token()
        self.assertEqual(result, "NOT_VALID_TOKEN")
