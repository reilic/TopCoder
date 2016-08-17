#lvl7 
#Count the Digit
def nb_dig(n, d):
	result= ""
	count = 0

	for i in range(n+1):
		result = result + str(i**2)

	for i in result:
		if i == str(d):
			count += 1

	return count

#lvl7
#Money,Money,Money
def calculate_years(principal, interest, tax, desired, count=0):

	if principal >= desired:
		return count

	principal = principal * (1 + interest) - (principal * interest * tax)

	return calculate_years(principal, interest, tax, desired, count+1)

#lvl7
#Vampire Numbers
def Vampire_Numbers(x,y):
	input = str(x)+str(y)
	output = str(x*y)

	return sorted(input) == sorted(output)

#lvl6
#Dbftbs Djqifs
def encryptor(key,message):
	enc =[]
	for e in message:
		if e.isalnum():
			enc.append(chr(ord(e)+key))
		else:
			enc.append(e)
	print enc

#lvl7
#Jaden Casing Strings
def toJadenCase(s):
	result = ''
	for e in s.split(' '):
		result = result + e[0].upper() + e[1:].lower() +' '

	return result[:-1]

#lvl6
#Multiplication Tables
def multiplication_table(row,col):
	result = []
	for r in range(1,row+1):
		inner =[]
		for c in range(1,col+1):
			inner.append(r*c)
		result.append(inner)
	return result

#lvl7
#List Filtering
def filter_list(l):

	print l

	for i in range(len(l)-1,0,-1):
		if not (type(l[i]) is int):
			l.pop(i)

	return l