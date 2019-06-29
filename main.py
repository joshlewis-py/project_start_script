import sys
import os
import getpass
from github import Github
import subprocess


path = ("/home/osboxes/Documents/Projects/")


def verification():
	# Check if file already exsists and if there is an arguement in the connand.
	while True:
		if len(sys.argv) > 1:
			x = str(sys.argv[1])

			if os.path.exists(path+x):
				print("file already exists, try again")
				x = input("Project title: ")

			else:
				github(x)
				break

		else:
			x = input("project title: ")
			if os.path.exists(path+str(x)):
				print("file already exists, try again")

			else:
				github(x)
				break


def github(x):
	# Github Login, maybe uselss but I like it.
	print("Enter your login details to create", x)
	username = input("Enter Github username: ")
	password = getpass.getpass("Enter Github password: ")
	create(x, username, password)


def create(x, username, password):
	# Get Github account and create repo named after the project.
	try:
		user = Github(username, password).get_user()
		repo = user.create_repo(x)

	except:
		print("Wrong login details, try again!")
		github(x)

	# Create folder and README.md file on the local system.
	os.makedirs(path+(str(x)))

	# subprocess.Popen("touch", "README.md", cwd="path+str(x)")
	# git init
	# git remote add origin ........
	# f= open(path+(str(x))+"/README.md","w+")
	# git push -u origin master

	
	print("Succesfully created repository ", x)


if __name__ == "__main__":
	verification()
