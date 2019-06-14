import sys
import os
from github import Github

path = "/home/osboxes/Documents/Projects/"

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(sys.argv[1]))
    print("Succesfully created repository {}".format(sys.argv[1]))

if __name__ == "__main__":
	create()
