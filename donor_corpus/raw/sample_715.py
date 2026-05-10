#!/bin/python3

import sys
import socket
from datetime import datetime

#Defining our target
if len (sys.argv) == 2:
	target=socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
	print("invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")


#add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " +str(datetime.now()))
print("-"*50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))# returns an error indicator
		if result ==0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\n Exiting program...")
	sys.exit()

except socket.gaierror:
	print("\n Hostname could not be resolved...")
	sys.exit()

except socket.gaierror:
	print("\n Could not connect to server...")
	sys.exit()

