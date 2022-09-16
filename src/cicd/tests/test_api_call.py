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
        """
        from cicd.github import GithubRepoClass
        github = GithubRepoClass('amirmahdy', 'market_data_provider')
        result = github.call_api()
        self.assertEqual(result.status_code, 200)

    def test_call_api_private(self):
        """
        This test checks if using the above token we can get a result from call_api method
        """
        from cicd.github import GithubRepoClass
        github = GithubRepoClass('amirmahdy', 'order_bird')
        result = github.call_api()
        self.assertIn(result.status_code, [401, 404])