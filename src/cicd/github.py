from cicd.models import Repo


class Github:
    def __init__(self, owner, repo) -> None:
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
