import random
st=int(input("Enter the starting value   :"))
en=int(input("Enter the Ending value     :"))
ch=int(input("Enter the number of chances:"))
n=random.randint(st,en)#st and en also taken
chance=1
while (chance<=ch):
	a=int(input("Enter the Number:"))
	if(chance<ch):
		if (n == a):
			print("You've won 😀️")
			break
		else:
			print("Try again")		
	if (chance == ch and n==a):
		print("You've won 😀️")
		break
	chance+=1
if (chance>ch):
	print("Oh ! You've Lost 😭️ and the number is", n)

