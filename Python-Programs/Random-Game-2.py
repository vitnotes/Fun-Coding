import random
times=int(input("Enter How many times you want to play this game:"))
i=0
pts=0
while (i<times):
	st=int(input("Enter the starting value   :"))
	en=int(input("Enter the Ending value    :"))
	ch=int(input("Enter the number of chances:"))
	n=random.randint(st,en)#st and en also taken
	chance=1
	while (chance<=ch):
		a=int(input("Enter the Number:"))
		if(chance<ch):
			if (n == a):
				pts+=1
				print("You've won 😀️")
				break
			else:
				print("Try again")		
		if (chance == ch and n==a):
			pts+=1
			print("You've won 😀️")
			break
		chance+=1
	if (chance>ch):
		print("Oh ! You've Lost 😭️ and the number is", n)
	i+=1
print("You've got", pts,"out of",times)
