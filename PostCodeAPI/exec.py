from sys import argv
import urllib2
import json

#accept user input argv
#get postcode info
#determine if result is valid

script, postcode = argv
data = None


url = 'http://v0.postcodeapi.com.au/suburbs/%s.json' % postcode
header = {'User-Agent' : 'ubuntu Browser'}

req = urllib2.Request(url, headers=header)

opener = urllib2.build_opener()

try:
	data = json.loads(opener.open(req).read())
except urllib2.HTTPError, e:
	print "Request doesn't generate anything."

if data:
	for e in data:
		print e['name']
else:
	print "no data"
	
