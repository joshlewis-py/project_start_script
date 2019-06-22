import sys
import os
import os.path
import getpass
from github import Github

path = ("/home/osboxes/Documents/Projects/")


def verification():
	# check if file already exsists and if there was paramenter in the connand
	while True:
		if len(sys.argv) > 1:
			x = str(sys.argv[1])

			if os.path.exists(path+x):
				print("file already exists, try again")
				x = input("Project title: ")

			else:
				print("the project is called ", x)
				github(x)
				break

		else:
			x = input("project title: ")

			if os.path.exists(path+str(x)):
				print("file already exists, try again")
				x = input("Project title: ")

			else:
				print("the project is called ", x)
				github(x)
				break


def github(x):
	print("Enter your login details to create", x)
	# need to check if details are correct
	username = input("Enter Github username: ")
	password = getpass.getpass("Enter Github password: ")
	create(x, username, password)


def create(x, username, password):
	# create folder and readme file on the system
	os.makedirs(path+(str(x)))

	# Get Github account and create repo named after the project
	user = Github(username, password).get_user()
	repo = user.create_repo(x)
	print("Succesfully created repository ", x)


if __name__ == "__main__":
	verification()
