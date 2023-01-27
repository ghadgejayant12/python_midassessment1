#Create function to check if date is in given range
from datetime import datetime

choose='y'
while choose=='y' and choose=='Y':
	y1,m1,d1 = list(map(int,input('Enter year month and day').split()))
	y2,m2,d2 = list(map(int,input('Enter year month and day').split()))
	date1=datetime(y1,m1,d1)
	date2=datetime(y2,m2,d2)
	num=int(input('Enter the number of dates to check :'))
	for i in range(num):
		y3,m3,d3=list(map(int,input('Enter year month and day').split()))
		date3=datetime(y3,m3,d3)
		print(date3<=date2 and date3>=date1)
		print('--------------------------')
	choose=input('Do you want to continue? (y/n)')