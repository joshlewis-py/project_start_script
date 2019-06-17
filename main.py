import sys
import os
import getpass
from github import Github
from pathlib import Path






def create():

	# If no parameters passed ask for a project name and check if file already there
		
	
	if len(sys.argv) > 1:
		x = sys.argv[1]

		print("the project folder and repository will be called ", x)
	else:
		x = input("Project tile: ")







	
	# I want to somehow verify username and passord

	username = input("Enter Github username: ")
	password = getpass.getpass("Enter Github password: ")

	path = ("/home/osboxes/Documents/Projects/"+str(x))

	# Make folder named parameter, os.makedirs(path + str(x))	
	os.makedirs(path)
	
	# Get Github account and create repo after the parameter
	user = Github(username, password).get_user()
	repo = user.create_repo(x)
	
	print("Succesfully created repository ", x)

	
if __name__ == "__main__":
	create()
