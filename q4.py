# Question : Create function to generate data randomly with python standard library
from random import randint
choose='y'
while choose=='y' or choose=='Y':
	st,ed = list(map(int,input('Enter the range in which to generate : ').split()))
	num=int(input('Enter the size of list :'))
	print([randint(st,ed) for i in range(num)])
	choose=input('Do you wish to continue? (y/n) : ')