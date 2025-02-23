d=int(input("Enter the date :"))
m=int(input("Enter the month:"))
y=int(input("Enter the year :"))
modd = [1,3,5,7,8,10,12]
meven = [4,6,9,11]
if m in modd and d>0 and d<31:
	d+=1
elif m in modd and d==31:
	d=1
	m+=1
elif m in meven and d>0 and d<30:
	d+=1
elif m in meven and d==30:
	d=1
	m+=1
elif m==2:
	if(( y%400 == 0)or (( y%4 == 0 ) and ( y%100 != 0))):
		if(d>0 and d<29):
			d+=1
		elif d==29:
			d=1
			m+=1
	else:
		if(d>0 and d<28):
			d+=1
		elif d==28:
			d=1
			m+=1
elif d==31 and m==12:
	d=1
	m=1
	y=y+1
print (d,m,y)
