import sys
import urllib
import json
import time
from jinja2 import Template
import requests
import hashlib
import subprocess

def checksum(f):
        md5 = hashlib.md5()
        md5.update(open(f).read())
        return md5.hexdigest()
#for i in sys.argv[1:]:
template = urllib.urlopen("http://my_example/template.txt").read()
f = open("/home/vagrant/template.txt", "wb")
f.write(template)
f.close()

res = ""
for i in sys.argv[1:]:
	with open("/home/vagrant/template.txt") as myFile:
	        templateStr = myFile.read()
        	template = Template(templateStr)

	domain = i
	fileName = '/home/vagrant/example/nginx.'+domain+'.txt'
	with open(fileName, 'w') as myFile:
	        myFile.write(template.render(my_domain=domain))
	if i != len(sys.argv):
		res += i + " " + checksum(fileName) + " "
	else: res += i + " " + checksum(fileName) 

print res
