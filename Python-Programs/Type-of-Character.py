ch = input("Enter the character:")
if (ch>'a' and ch<'z'):
	print("It's in lowercase")
elif(ch>'A' and ch<'Z'):
	print("It's in Uppercase")
elif(ch>'0' and ch<'9'):
	print("It's a number")
else:
	print("It's a special character")

