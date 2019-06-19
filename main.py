import sys
import os
import getpass
from github import Github


x = "defult"
path = ("/home/osboxes/Documents/Projects/"+str(x))


def verification():

	# check if x already exsists and if there was paramenter in the connand





	if len(sys.argv) > 1:
		x = sys.argv[1]

		if os.path.exists(path):
			print("File already exsists try again")

		else:
			print("The project folder and repository will be called", x)



	else:
		x = input("Project tile: ")
		if not os.path.exists(path):
			print("File already exsists try again")

		else:
			print("The project folder/repository will be called", x)




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
