#!/bin/python3

import sys 
import socket
from datetime import datetime
from time import sleep

def quit():
	print("\nQuitting...")
	sleep(0.80)
	sys.exit()

#Define our target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate host name to IPv4

else:
	print("\nError: Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
	quit()

#Add a banner
print("-" * 50)
print("Initiating Python Scanner")
print("...")
sleep(0.80)
print("Scanning target \"" + target + "\"")
print("Time started at: " + str(datetime.now()))
print("-" * 50)

port1 = int(input("Select first port (included): "))
port2 = int(input("Select last port (not included): "))


try:
	for port in range(port1, port2):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #float: ex 0.5
		result = s.connect_ex((target, port)) #return error indicator
		
		print("Checking port {}".format(port))
		if result == 0:
			port = print("Port {} is open".format(port))
		s.close()

#Keyboard Interrupt err
except KeyboardInterrupt:
	quit()
	
#No hostname err
except socket.gaierror:
	print("Hostname could not be resolved")
	quit()

#No connection / server down err
except socket.error:
	print("Could not connect to server")
	quit()
