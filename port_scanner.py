# write a program to check ports 80, 443 on a host (e.g., "local host").
#Use socket to test connections

#load socket module
import socket

#identifies the computer im working on
host = "localhost"

#create a list of ports to test
ports = [80,443]

#creates a socket then stores it in a variable
s = socket.socket()

#loop through each port one at a time
for port in ports:

   # Try connecting to host and port + store results
   result= s.connect_ex ((host,port))

# If Else statement telling vs code what to do if the port is open or  not
   
   # ' == 0 ' Means if connection was successful
   if result == 0:

    # Uses an F string to insert a port number and lets me know if the port is open
    print (f"port {port} is open")

   else:

    # Prints if any port is closed
     print (f"port{port} is closed")


