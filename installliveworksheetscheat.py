from git import Repo
import os
git_url = "https://github.com/RealNattawattHongthong/liveworksheet-cheat.git"
repo_dir = "liveworksheets-cheat"
Repo.clone_from(git_url, repo_dir)