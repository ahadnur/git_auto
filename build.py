from github import Github
import os
import time
from datetime import timezone
import datetime



__version__ = "1.0.0"


dt = datetime.datetime.now(timezone.utc)
utc_time = dt.replace(tzinfo=timezone.utc)
utc_timestamp = utc_time.timestamp()

fileName = "daemon_proj_{}_{}".format(__version__, utc_timestamp)

# Create zip file and send it to build directory
def zip(filename):
    # check the directory
    print("Making the zip file...")
    make_zip = f"zip -r {filename}.zip src"
    os.system(make_zip)
    print("Completed zip creation.")
    move_zip = "mv {}.zip build".format(filename)
    os.system(move_zip)


# login to github
def login(AccessToken):
    try:
        g = Github(AccessToken)
        user = g.get_user("ahadnur")
        user.login
        print(f"Login confirmed as {user.name}")
    except Exception as e:
        print(e)





# get the filename from git
def add_to_git(filename):
    add_command = "git add ."
    os.system(add_command)
    commit_command = "git commit -m 'new file updated{}'".format(filename)
    print("All set. Push It to the git repo with git push")
        


# Update the file to git


if __name__ == '__main__':
    start_time = time.time()

    accessToken = "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"
    login(accessToken)

    filename = fileName
    zip(filename)
    add_to_git(filename)
    ending_time = time.time()

    print("Program took {}s".format(round(ending_time-start_time, 3)))
