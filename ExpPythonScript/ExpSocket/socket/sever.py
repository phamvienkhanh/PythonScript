import socket
import sys
import thread

# Create a TCP/IP socket ==================================================
sock 			= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverAddress 	= ('127.0.0.1',10000)

print >>sys.stderr, 'starting up on %s port %s ' % serverAddress

sock.bind(serverAddress)
#=========================================================================

# create List client ======================================================
listClient = ()
sock.listen(5)

def listenConnectClient():
	global listClient
	global sock

	while True:
		#wait for a connection
		#print >>sys.stderr, 'waitting for a connection '
		newConn 	= ()
		newConn 	= sock.accept()
		#print >> sys.stderr, 'connection from ', newConn[1]
		if newConn not in listClient:
			listClient += newConn
#==========================================================================


# Listen for incoming connections =========================================
def sendMessage():
	while True:
		# Receive and send data
		try:
			#data = connection.recv(255)
			data = raw_input('==|> ')
			#print >>sys.stderr, 'received ==|> %s ' % data
			if data:
				#print >> sys.stderr, 'sending data back to the client '
				for clientConn in listClient:
					proc	 = clientConn
					print >> sys.stderr, 'connection from ', proc
					try:
						proc.sendall(data)
					except:
						pass
			else:
				#print >>sys.stderr, ' no more data from ', clientAddress
				break
		finally:
			# Clean up the connection
			#connection.close()
			pass
#==========================================================================

# Start thread listen Connect client ======================================
try:
	thread.start_new_thread(listenConnectClient, ())
	thread.start_new_thread(sendMessage, ())
except:
	pass
#==========================================================================

while 1:
	pass