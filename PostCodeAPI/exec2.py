from sys import argv
import json
import requests


#accept user input argv
#get postcode info
#determine if result is valid

script, postcode = argv
data = None

url = 'http://v0.postcodeapi.com.au/suburbs/%s.json' % postcode
header = {'User-Agent' : 'ubuntu Browser'}
response = requests.get(url,headers=header)

#if successful retrieve

if response.status_code != 200:
	print "no data"
else:
	data = json.loads(response.text)
	for e in data:
		print e['name']
