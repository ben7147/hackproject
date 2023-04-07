from git import Repo
import os
git_url = "git clone https://github.com/Z4nzu/hackingtool.git"
repo_dir = "hackingtool"
Repo.clone_from(git_url, repo_dir)
os.system('chmod -R 755 hackingtool')
os.chdir("hackingtool")
os.system('sudo bash install.sh')
