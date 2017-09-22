import socket
import sys

# Create a TCP/IP socket ==============================================
sock 	= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the IP and port where the server is listening
severAddress = ('127.0.0.1',10000)
print >>sys.stderr, 'connecting to %s port %s ' % severAddress
sock.connect(severAddress)

# Send and recevie data ===============================================
while True:
	try:
		data = sock.recv(255)
		print >>sys.stderr,'<|== %s '% data
		# send data
		#message = raw_input(' ==|> ')
		#print >>sys.stderr,'sending ==|> %s' % message
		#sock.sendall(message)

		# Look for the response
		#amountRececived 	= 0
		#amountExpected 		= len(message)

		#while amountRececived<amountExpected:
		#	data = sock.recv(255)
		#	amountRececived += len(data)
		#	print >>sys.stderr, ' <|== %s ' % data
	except:
		#print >>sys.stderr, 'closing socket '
		#sock.close()
		pass