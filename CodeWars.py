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

	print count