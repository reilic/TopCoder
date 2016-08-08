def this():
	
	result = ['apple','orange','pear']
	
	for i in range(10):
	
		result.append(str(i))

	#print result

	print "-".join(result)

	for index, value in enumerate(result):
		print '%d %s' % (index, value)

	print 'test'