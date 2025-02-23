v=0
name=input("Enter your name:")
for i in name:
	if i in ('a','e','i','o','u'):
		v+=1
else:
	print("Iteration Completed")
print("The name",name,"has",v,"vowels")
