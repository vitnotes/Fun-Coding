n=int(input("Enter the number:"))
rev=0
num=n
while (num):
	digit=num%10
	rev=rev*10+digit
	num=num//10
if (rev==n):
	print("Palindrome 😁️")
else:
	print("Not a Palindrome 😭️")
