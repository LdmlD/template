import sys
import os
import os.path
import hashlib
import paramiko
from exceptions import Exception
import urllib
import requests

#f = open('/home/vagrant/smth')
user = 'vagrant'
passw = 'vagrant'
port = 22
path = '/etc/nginx/nginx.conf'



def connection():
	hosts=[]
	for i in sys.argv[1:]:
		hosts.append(i)
        for i in range(len(hosts)):
		host = str(hosts[i])
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(hostname=host, username=user, password=passw, port=port)
		myCommand = 'curl -f http://my_example/nginx.'+host+'.txt -o /etc/nginx/nginx.conf'
		client.exec_command(myCommand)
		client.close()

	
connection()
