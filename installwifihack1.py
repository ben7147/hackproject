from git import Repo
import os
git_url = "https://github.com/ZKAW/wifi-deauther.git"
repo_dir = "wifi-deauther"
Repo.clone_from(git_url, repo_dir)
os.chdir("wifi-deauther")
os.system('chmod +x INSTALL')
os.system('sudo ./INSTALL')