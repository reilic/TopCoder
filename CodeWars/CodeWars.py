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

#lvl6
#Vasya-Clerk
def tickets(people):
	change = 0
	ticket_price = 25 #ticket is $25 dollars

	print people

	if people[0] > ticket_price:
		return 'NO'

	for p in people:
		if p == ticket_price:
			#exact amount
			change += p
		else:
			#need change given
			change -= (p - ticket_price)

	print change
	return 'YES' if change >=0 else 'NO'

#lvl6
#Unique in Order
#example: AAAABBBCCCcccDAABB should return A,B,C,c,D,A,B.
def unique_in_order(iterable):

	if iterable:

		answer =[iterable[0]]

		for e in iterable:
			if e != answer[-1]:
				answer.append(e)

		return answer

	return []

#lvl5
#Gap in Primes
def gap (g,m,n):

	result =[]
	final = []

	#populate all prime numbers in range
	for i in range(m,n+1):
		if isprime(i):
			result.append(i)

	for i in range(0,len(result)-1):
		if result[i] + g == result[i+1]:
			final.append(result[i])
			final.append(result[i+1])
			break

	if final == []:
		return None
	else:
		return final

def isprime(i):
	if i < 2: return False
	if i == 2: return True

	for n in range(2,i):
		if i % n == 0:
			return False
	return True

#lvl6
#Complete the Pattern #8 - Number pyramid
def pattern(n):
	result = ""

	if n == 1: return "1"
	if n == 0: return result

	for i in range(1,n+1):
		result = result + " "*(n-i) + str(prt(i)) + " "*(n-i) + "\n"
	return result


def prt(i):
	s = ''
	for i in range(1,i+1):
		s = s + str(i)

	for i in range(i,1, -1):
		s = s + str(i-1)
	return s