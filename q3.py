# Question : [1,2,3,1,3,4,6,5,3] get unique numbers from list with basic constructs
from collections import defaultdict


given=[1,2,3,1,3,4,6,5,3]
print('Original List given :',given)

ans=defaultdict(lambda : 0)

for i in given:
	ans[i]=ans[i]+1
	pass

unique = [key for key,val in ans.items() if val==1]
print('Unique numbers are :',unique)