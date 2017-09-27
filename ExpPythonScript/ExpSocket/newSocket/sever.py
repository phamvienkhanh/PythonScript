import socket
import sys
import thread

# Create a TCP/IP socket ==================================================
sock 			= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverAddress 	= ('127.0.0.1',10000)

print >>sys.stderr, 'starting up on %s port %s ' % serverAddress

sock.bind(serverAddress)
#=========================================================================

# List client connect have create thread =================================
listConnected = []
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

# Listen and recevie message from client ==================================
def listenMessageClient(connection):
	while True:
		try:
			data = connection.recv(255) #recevie mess
			if data:
				for ortherClient in listClient:
					if ortherClient != connection:
						try:
							ortherClient.sendall(data)
						except:
							pass
		except:
			pass
#==========================================================================

# Listen for incoming connections =========================================
def createThreadsClient():
	global listConnected
	while True:
		try:
			for clientConn in listClient:
				if(clientConn not in listConnected):
					try:
						thread.start_new_thread(listenMessageClient,(clientConn,))
						listConnected.append(clientConn)
					except:
						pass
		finally:
			pass
#==========================================================================




# Start thread listen Connect client ======================================
try:
	thread.start_new_thread(listenConnectClient, ())
	thread.start_new_thread(createThreadsClient, ())
except:
	pass
#==========================================================================

# Program never close
while 1:
	pass