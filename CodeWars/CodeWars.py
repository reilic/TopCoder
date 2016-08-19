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
	for i in range(len(l)-1,-1,-1):
		if not (type(l[i]) is int):
			l.pop(i)

#lvl6
#Your order, please
def order(sentence):

	s = sentence.split(" ")
	ordered = []

	for i in range(1,len(s)+1):
		for e in s:
			for c in e:
				if c == str(i):
					ordered.append(e)

	return " ".join(ordered)

#lvl6
#Persistent Bugger
def persistence(n, count=0):
	num = []
	total = 1

	#when n is 1-digit 
	if n < 10:
		return count

	#load number as individual digits
	for e in str(n):
		num.append(e)

	for e in num:
		total *= int(e)

	return persistence(total,count+1)	

#lvl6
#Tortoise racing
def race(v1,v2,g):
	time = []

	if v1 >= v2:
		return None

	#since it's only int(), would return only integers which represents the hour	
	time.append(g/(v2 - v1))

	time_taken = g/float(v2 - v1) #in hour

	#min taken
	time.append(int(time_taken * 60 % 60))

	#sec taken
	time.append(int(time_taken * 60 % 60 * 60 % 60))
	
	return time

