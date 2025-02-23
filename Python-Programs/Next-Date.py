import sys
d=int(input("Enter the date :"))
m=int(input("Enter the month:"))
y=int(input("Enter the year :"))
m31=[1,3,5,7,8,10]
m3=[1,3,5,7,8,10,12]
m30=[4,6,9,11]
if (m in m3) and (d>0 and d<31):
	d+=1
elif (m in m31) and (d==31):
	d=1
	m+=1
elif (m in m30) and (d>0 and d<30):
	d+=1
elif (m in m30) and (d==30):
	d=1
	m+=1
elif (m==2) and (y%400==0 or (y%4==0 and y%100!=0)) and (d>0 and d<29):
	d+=1
elif (m==2) and (y%400==0 or (y%4==0 and y%100!=0)) and (d==29):
	d=1
	m+=1
elif (m==2) and (d>0 and d<28):
	d+=1
elif (m==2) and (d==28):
	m+=1
	d=1
elif (m==12) and (d==31):
	d=1
	m=1
	y+=1
else:
	print("Invalid date")
	sys.exit()
print("The next date is",d,'-',m,'-',y,)
