from cicd.models import Repo, GithubToken
from utils.request_handler import RequestHandler


class GithubRepos:
    def __init__(self, owner, repo) -> None:
        self.request_handler = RequestHandler()
        self.owner = owner
        self.repository = repo
        self.header = None
        self.url = f"https://api.github.com/repos/{owner}/{repo}"
        self.get_token()

    def get_token(self):
        """
        TODO This method should decrypt token by secret_key.
        """
        self.repo_db = Repo.objects.filter(owner=self.owner, repository=self.repository)
        if len(self.repo_db) == 0:
            return False
        elif self.repo_db.first().token is None:
            return None
        else:
            self.header = {"Authorization": f"Bearer {self.repo_db.first().token.token}"}
            return self.repo_db.first().token.token

    def call_api(self):

        if self.repo_db.first() is None or self.header is None:
            result = self.request_handler.get(self.url)
            """
            TODO Add non existent URL to our DB
            """
        elif self.header is not None:
            result = self.request_handler.get(self.url, self.header)

        return result


class GithubTokens:
    def __init__(self) -> None:
        pass

    @staticmethod
    def add_token(name, token):
        """
        TODO This method should decrypt token by secret_key.
        """
        return GithubToken.objects.create(name, token)
