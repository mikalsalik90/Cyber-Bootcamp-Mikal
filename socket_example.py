import socket

# ^ Create a TCP socket
s = socket.socket()

# Optional: set timeout so it does'nt hang and crash
s.settimeout(1)# ".settimeout" not s.settimeout

# Test connection to localhost port 80
result = s.connect_ex(("localhost", 80))

#Print whether the port is open or closed 
if result == 0:
    print("port 80 is open")
else:
    print("Port 80 is closed")

s.close()