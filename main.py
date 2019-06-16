import sys
import os
import getpass
from github import Github

path = "/home/osboxes/Documents/Projects/"

def create():

	# If no parameters passed ask for a project name
	if len(sys.argv) > 1:
		x = sys.argv[1]
		print("the project folder and repository will be called ", x)
	else:
		x = input("Project tile: ")
	
	# I want to somehow verify username and passord
	username = input("Enter Github username: ")
	password = getpass.getpass("Enter Github password: ")

	# Make holder named parameter	
	os.makedirs(path + str(x))
	
	# Get Github account and create repo after the parameter
	user = Github(username, password).get_user()
	repo = user.create_repo(x)
	
	print("Succesfully created repository ", x)

	
if __name__ == "__main__":
	create()
