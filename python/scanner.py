#!/bin/python3
import sys
import socket
from datetime import datetime 

# Target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>.")

# Pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: "+ str(datetime.now()))
print("-" * 50)

try:
    for port in range(50,85):
        s = socket.socket(socker.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) # Returns an error indicator 
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Couldn't connect to server")
    sys.exit()
