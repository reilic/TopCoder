from sys import argv
import urllib2
import json

#accept user input argv
#get postcode info
#determine if result is valid

script, postcode = argv
data = []


url = 'http://v0.postcodeapi.com.au/suburbs/%s.json' % postcode
header = {'User-Agent' : 'ubuntu Browser'}

req = urllib2.Request(url, headers=header)

opener = urllib2.build_opener()

try:
	data = json.loads(opener.open(req).read())
except urllib2.HTTPError, e:
	print "Request doesn't generate anything."

print data

if data == []:
	print "no data"
else:
	print data[0]['name']

