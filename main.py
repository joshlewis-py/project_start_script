import sys
import os
import getpass
from github import Github

path = "/home/osboxes/Documents/Projects/"

def create():

	if len(sys.argv) > 1:
		x = sys.argv[1]
		print("the project folder and repository will be called ", x)
	else:
		x = input("Project tile: ")

	
	username = input("Enter Github username: ")
	password = getpass.getpass("Enter Github password: ")
	repo = user.create_repo(x)
	folderName = str(x)
	os.makedirs(path + str(x))
	user = Github(username, password).get_user()
	
	print("Succesfully created repository ", x)

	
if __name__ == "__main__":
	create()
