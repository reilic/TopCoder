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

	#test

#Money,Money,Money

def calculate_years(principal, interest, tax, desired, count=0):

	if principal >= desired:
		return count

	principal = principal * (1 + interest) - (principal * interest * tax)

	return calculate_years(principal, interest, tax, desired, count+1)
