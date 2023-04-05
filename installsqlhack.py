from git import Repo
import os
git_url = "https://github.com/sqlmapproject/sqlmap.git"
repo_dir = "sql-hack"
Repo.clone_from(git_url, repo_dir)