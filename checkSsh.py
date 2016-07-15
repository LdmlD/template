import sys
import os
import os.path
import paramiko
from exceptions import Exception

hosts = []
sums = []
for i in range(len(sys.argv)):
	if  i%2 != 0:
		hosts.append(sys.argv[i])
		sums.append(sys.argv[i+1])

#hosts = ["192.168.1.20","192.168.1.30"]
user = 'vagrant'
passw = 'vagrant'
port = 22

def connection():
        checkFiles = {}
        for i in range(len(hosts)):
                host = str(hosts[i])
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(hostname=host, username=user, password=passw, port=port)
                stdin, stdout, stderr = client.exec_command('md5sum /etc/nginx/nginx.conf')
                data = stdout.read()
                checkFiles[i] = data
                client.close()
        return checkFiles

def checkCopies():
	for i in range(len(sums)):
		sums[i]+="  /etc/nginx/nginx.conf\n"

	checkFiles = connection()
  	c = 0
	resList = []
	for i in range(len(hosts)):
                fileToCheck1= hosts[i]
               	if (str(checkFiles[i])!=str(sums[i])):
			resList.append(hosts[i])
			c +=1
	if c==0:
		print("All files are correct.")
	res=""
	for i in range(len(resList)):
		if i!=len(resList):
			res += str(resList[i]) +" "
		else: res += str(resList[i])
	print res

checkCopies()

