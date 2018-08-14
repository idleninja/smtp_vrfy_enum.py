#!/bin/python

import smtplib, os, sys

def printBanner():
	print("*" * 50)
	print("* %s " % "Welcome to the SMTP Vrfy enum script.")
	print("* python %s %s " % (sys.argv[0], "to start execution."))
	print("*" * 50)


def getUserInput(msg="Default message: "):
    return raw_input(msg).strip()

def pullFileList(file_path=""):
	file_contents = ""
	if os.path.isfile(file_path):
		with open(file_path, "r") as f:
			file_contents = f.read().splitlines()
	return file_contents

def vrfyUser(user="", smtp_server=""):
	if user and smtp_server:
		if "250" not in str(smtp_server.vrfy(user)[0]):
			return False
		else:
			return True
	else:
		return None

def main():
	printBanner()

	server = getUserInput("SMTP Server to VRFY users: ")
	if server:
		smtp_server = smtplib.SMTP(server)
	else:
		print("Unable to connect to %s." % server)
		exit()

	valid_users = set()
	users = pullFileList(getUserInput("Path to users list: "))
	users = set([user.strip() for user in users if user])
	for user in users:
		if user and vrfyUser(user, smtp_server):
			print("%s is a valid user" % user)
			valid_users.add(user)
		else:
			print("%s is not a valid user or failed to connect." % user)

	print("\n\nValid Users:")
	print("\n".join(valid_users))

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt):
        print("^C")
        exit()
