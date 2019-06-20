import sys
import os
import os.path
import getpass
from github import Github

path = ("/home/osboxes/Documents/Projects/")

def verification():

	# check if x already exsists and if there was paramenter in the connand
	x = str(sys.argv[1])
	while True:
		if len(sys.argv) > 1:
			if os.path.exists(path+x):

				print("file already exists, try again")
				x = input("Project title: ")

			else:
				print("the project is called ", x)
				break




		else:
			x = input("project title: ")

			if os.path.exists(path+x):
				print("file already exists, try again")
				x = input("Project title: ")

			else:
				print("the project is called ", x)
				break








	# need to check if file already exsists
	username = input("Enter Github username: ")
	password = getpass.getpass("Enter Github password: ")
	create(x, username, password)



def create(x, username, password):

	# I want to somehow verify username and passord


	# Make folder named parameter, os.makedirs(path + str(x))
	os.makedirs(path)

	# Get Github account and create repo after the parameter
	user = Github(username, password).get_user()
	repo = user.create_repo(x)

	print("Succesfully created repository ", x)



if __name__ == "__main__":
	verification()
