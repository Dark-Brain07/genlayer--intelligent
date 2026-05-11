# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class GithubRepoOracle(gl.Contract):
    """
    Chain Quest: GitHub Repo Oracle
    Fetches REAL GitHub repository data to generate
    developer-themed quests (stars = XP, forks = allies).
    """
    last_stars: str
    last_forks: str

    def __init__(self):
        self.last_stars = "0"
        self.last_forks = "0"

    @gl.public.write
    def fetch_repo_stats(self, owner: str, repo: str) -> str:
        url = "https://api.github.com/repos/" + owner + "/" + repo

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            stars = str(data["stargazers_count"])
            forks = str(data["forks_count"])
            return stars + "|" + forks

        result = gl.eq_principle.strict_eq(_fetch)
        parts = result.split("|")
        self.last_stars = parts[0]
        self.last_forks = parts[1]
        return "Stars: " + parts[0] + " | Forks: " + parts[1]

    @gl.public.view
    def get_stars(self) -> str:
        return self.last_stars
