d=int(input("Enter the date :"))
m=int(input("Enter the month:"))
y=int(input("Enter the year :"))
if m == (1,3,5,7,8,10,12):
	ml=31
elif m==2:
	if y%4 ==0 or y%400 ==0 and y%100!=0:
		ml=29
	else:
		ml=28
elif m in (4,6,9,11):
	ml=30
if d>0 and d<ml:
	d+=1
elif d==ml:
	if m==12:
		d=1
		m=1
		y+=1
	else:
		d=1
		m+=1	
print("The next date is",d,'-',m,'-',y)
