# Question : [“name512”, “same1example”, “joy18full”] replace the digits from string inside list

given=['name512', 'same1example', 'joy18full']
print('Original List :',given)

for i in range(len(given)):
	result=''
	for letter in given[i] :
		if ord(letter)<=57 and ord(letter)>=48:
			result=result+' '
		else:
			result=result+letter
	given[i]=result.strip()
print('Altered List where digits have been replaced with space:',given)
print('---------------------------------------------------------------------------------')
given=['name512', 'same1example', 'joy18full']
print('Original List :',given)

for i in range(len(given)):
	result=''
	for letter in given[i] :
		if not (ord(letter)<=57 and ord(letter)>=48):
			result=result+letter
	given[i]=result.strip()
print('Altered List where digits have been removed:',given)
