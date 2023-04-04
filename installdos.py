from git import Repo
import os
git_url = "https://github.com/palahsu/DDoS-Ripper.git"
repo_dir = "DDoS-Ripper"
Repo.clone_from(git_url, repo_dir)