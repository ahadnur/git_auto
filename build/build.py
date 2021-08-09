from github import Github
import os
import zipfile
from datetime import timezone
import datetime

version = "1.0.1"


dt = datetime.datetime.now(timezone.utc)

utc_time = dt.replace(tzinfo=timezone.utc)
utc_timestamp = utc_time.timestamp()

# Declare the function to return all file paths of the particular directory


def retrieve_file_paths(dirName):

    # setup file paths variable
    filePaths = []

    # Read all directory, subdirectories and file lists
    for root, directories, files in os.walk(dirName):
        for filename in files:
            # Create the full filepath by using os module.
            filePath = os.path.join(root, filename)
            filePaths.append(filePath)

    # return all paths
    return filePaths


file_name = "daemon_proj_{}_{}".format(version, utc_timestamp)


def zip():
    # Assign the name of the directory to zip
    dir_name = '/home/Desktop/pygithub/src'

    # Call the function to retrieve all files and folders of the assigned directory
    filePaths = retrieve_file_paths(dir_name)

    # printing the list of all files to be zipped
    print('The following file will be zipped:')
    for fileName in filePaths:
        print(fileName)

    # writing files to a zipfile
    zip_file = zipfile.ZipFile(file_name+'.zip', 'w')
    with zip_file:
        # writing each file one by one
        for file in filePaths:
            zip_file.write(file)

    print(dir_name+'.zip file is created successfully!')


def get_filename_from_git(access_token):
    g = Github(access_token)
    user = g.get_user("ahadnur")
    user.login

    path_for_del = 'daemon_proj_1.0.1_1628148657.115513.zip'

    repo = g.get_repo('ahadnur/git_auto')
    contents = repo.get_contents("")

    zip_path = repo.get_contents(path=path_for_del)
    file_name_git = zip_path.path

    zip_name = ""

    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            if file_content.name.__contains__('.zip'):
                zip_name = file_content.name

    return file_name_git


def upload_file_git(file_path, access_token):
    g = Github(access_token)
    user = g.get_user("ahadnur")
    user.login
    repo = g.get_repo('ahadnur/git_auto')
    print("Authenticated as {}".format(user.name))
    print("Uploading file {}.zip    ....".format(file_path))
    repo.create_file(file_path, "zip updated", "zip", branch="master")
    print("Uploading Complete")
    try:
        contents = repo.get_contents("/build")
        for c in contents:
            # print(c.path)
            if c.path.startswith("d"):
                repo.delete_file(c.path, message="file deleted", sha=c.sha)
                print(c.path, "Deleted...")

    except Exception as e:
        print(e)


# Call the main function
if __name__ == "__main__":
    zip()
    access_token = "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"
    file_path = "daemon_proj_{}_{}.zip".format(version, utc_timestamp)
    upload_file_git(file_path, access_token)
