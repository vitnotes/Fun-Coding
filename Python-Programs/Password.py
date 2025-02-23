import re
import getpass
p=getpass.getpass("Enter the password:")
x =True
while x:
	if len(p)<6:
		print("Enter the password which has more than six charaters")
		break
	elif not re.search("[A-Z]",p):
		print("Enter the password which has a Uppercase")
		break	
	elif not re.search("[a-z]",p):
		print("Enter the password which has a lowercase")
		break
	elif not re.search("[0-9]",p):
		print("Enter the password which has a Number")
		break	
	elif not re.search("[!@#]",p):
		print("Enter the password which has a special characters")
		break
	else:
		print("Password is valid 😁️")
		x =False
		break
if x:
	print("Password is invalid 😭️")
