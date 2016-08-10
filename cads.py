from sys import argv

doc = []

def loadfile(argv):

	script, filename = argv
	

	#List of lines that start with "Name"
	anchor =[] 

	#open file and read each line into doc[]
	with open(filename) as fp:
		for line in fp:			
			doc.append(line.splitlines())

	#find anchors for the lines that start with Name, and add into anchor[]
	for index,e in enumerate(doc[:30]):
		for c in e:
			if c[0:4] == 'Name':
				anchor.append(index)

	for a in anchor:
		format_for_upload(parse_anchor(a))

	fp.close()

def format_for_upload(source):
	print source
	print source[1:]
	#journal upload format
	#account, fund, dept, project,budget ref,amount, descr, line ref

	#account, and fund
	print ('%s,%s,') % (5312, str(source[0])),

	for i in source[1:]:

		print ('%s,') % i,

#	return source

def parse_anchor(anchor):
	snippet = []
	fund_code =''
	deptid = ''

	#fund code
	fund_code = str(doc[anchor-3]).replace(' ','')[7:8]
	snippet.append(fund_code) 
	
	#First 2 digits of deptid
	deptid = str(doc[anchor-2]).replace(' ','')[7:9]
	snippet.append(deptid) 
	
	#find the dotted line 
	limit = doc[anchor+2]

	#start from first GL combo
	anchor = anchor + 3

	while limit != doc[anchor]:
		#last 3 digits of department code
		snippet.append(str(doc[anchor])[2:5])

		#project id
		
		snippet.append(str(doc[anchor])[5:str(doc[anchor]).index(' ')])		
		
		#amount
		snippet.append(str(doc[anchor])[73:82].strip())

		anchor += 1

	return snippet