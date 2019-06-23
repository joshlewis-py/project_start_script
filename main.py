import sys
import os
import os
import getpass
from github import Github

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
	# Github Login, with verification.
	print("Enter your login details to create", x)

	while True:

		try:
			username = input("Enter Github username: ")
			password = getpass.getpass("Enter Github password: ")
			break

		except:
			print("Wrong login details, try again!")


	create(x, username, password)








def create(x, username, password):
	# Create folder and README.md file on the local system.
	os.makedirs(path+(str(x)))

	# Get Github account and create repo named after the project.
	user = Github(username, password).get_user()
	repo = user.create_repo(x)
	print("Succesfully created repository ", x)


if __name__ == "__main__":
	verification()
