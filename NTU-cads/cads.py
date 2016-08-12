from sys import argv
from selffunction import RemoveSpecialChars

doc = []
getmonth = ''
getyear = ''
total_amount = 0

def main(argv):

	script, filename = argv
	
	#List of lines that start with "Name"
	anchor =[] 

	#open file and read each line into doc[]
	with open(filename) as fp:
		for line in fp:			
			doc.append(line.splitlines())

	#find anchors for the lines that start with Name, and add into anchor[]
	for index,e in enumerate(doc[::]):
		for c in e:
			if c[0:4] == 'Name':
				anchor.append(index)

	#print journal template header
	print ('Account,Fund,Department,Project,BudgetRef,Amount,Descr,LineRef')

	#print all lines in the format for journal upload
	for a in anchor:
		format_for_upload(parse_anchor(a))

	#calculate offsetting amount in journal upload
	print ('Account,Fund,Department,Project,,-%s,ITS CADS %s %s,ITS-CADS') % (total_amount, getmonth, '20'+getyear)

	fp.close()

def parse_anchor(anchor):
	snippet = []
	
	fund_code = ''
	deptid = ''

	fund_anchor = ''
	deptid_anchor = ''

	#fund code anchor
	fund_anchor = anchor-3
	
	#set anchor for First 2 digits of deptid
	deptid_anchor = anchor-2
	
	#find the dotted line 
	limit = doc[anchor+2]

	#start from first GL combo
	anchor = anchor + 3

	global total_amount

	while limit != doc[anchor]:

		#don't load if fund is Unknown or if amount is 0.00
		if str(doc[fund_anchor]).replace(' ','')[7:14] != 'Unknown' and str(doc[anchor])[73:82].strip() !='0.00':
			
			#fund code
			snippet.append(str(doc[fund_anchor]).replace(' ','')[7:8])

			#department code
			snippet.append(str(doc[deptid_anchor]).replace(' ','')[7:9]+str(doc[anchor])[2:5])

			#project id
			snippet.append(RemoveSpecialChars(str(doc[anchor])[5:str(doc[anchor]).index(' ')]))		
			
			#amount
			total_amount += float(str(doc[anchor])[73:82].strip())
			snippet.append(str(doc[anchor])[73:82].strip())

		anchor += 1

	return snippet

def format_for_upload(source):
	
	#journal upload format
	#account, fund, dept, project,budget ref,amount, descr, line ref

	#find month/year using global variable
	global getmonth
	global getyear

	getmonth = str(doc[2])[18:20].strip()
	getyear = str(doc[2])[21:24].strip()

	for i in range(0,len(source))[::4]:

		print ('%s,%s,%s,%s,,%s,ITS CADS %s %s,ITS-CADS') % (5312, 
							str(source[i]),
							str(source[i+1]),
							str(source[i+2]),
							str(source[i+3]),
							getmonth,
							'20'+getyear)
