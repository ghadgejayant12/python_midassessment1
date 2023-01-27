#Question : [1, “a”, 2, “b”, 3, “c”] filter digits and alphabets separately using inbuilt functions like map, filter or reduce
given = [1,'a',2,'b',3,'c']


# Since alphabets have to be filtered they need to be strings of length 1 and must be between a and z  or between A and Z
def test_alphabets(element):
	if str(type(element))!="<class 'str'>":
		return False
	if len(element)==1 and (ord(element)<=122 and ord(element)>=97) or (ord(element)>=65 and ord(element)<=90):
		return True
	return False

# Since digits have to be filterd they must be numbers between 0 and 9
def test_digits(element):
	if str(type(element))!="<class 'int'>":
		return False
	if 0<=element<=9:
		return True
	return False

print('Original List :',given)
print('Filterd out the digits :',[i for i in filter(test_digits,given)],'(used filter function)')
print('Filterd out the alphabets :',[i for i in filter(test_alphabets,given)],'(used filter function)')

print('-----------------------------------------------------------')
digits=list()
alphas=list()

result=list(map(test_digits,given))
for i in range(len(result)):
	if result[i]:
		digits.append(given[i])
	else:
		alphas.append(given[i])

print('Original List :',given)
print('Filterd out the digits :',digits,'(used map function)')
print('Filterd out the alphabets :',alphas,'(used map function)')