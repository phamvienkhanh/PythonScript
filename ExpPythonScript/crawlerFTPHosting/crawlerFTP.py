'''
	script use to crawler hosting FTP, and find host can login anonymous
'''
#==== import ===================================================================
import random
from ftplib import FTP
from threading import Thread
#=== end import ================================================================

#=== define ====================================================================
MAX_TIME 	= 10000
MAX_THREAD	= 100
#=== end define ================================================================

#=== func getIp ================================================================
def getIp():
	""" random a ip adress and return """
	ip = ''
	for octan in xrange(0,3):
		ip += str(random.randint(0,255)) + '.'
	ip += str(random.randint(0,255))

	return ip
#=== end func getIp ============================================================

#=== func check FTP hosting ====================================================
def checkFTP(ip):
	""" check FTP and login """
	try:
		connection  = FTP(ip,timeout=2)
		wlcmMsg 	= connection.getwelcome()
		print(wlcmMsg)
		try:
			connection.login()
			with open("ListFTPHost.txt","a") as fileOut:
				fileOut.write(wlcmMsg + "\n")
				fileOut.write("FTP @ found : " + ip + "\n")
				fileOut.write("=============================================\n")
		except:
			pass
		connection.quit()
	except:
		pass
#=== end check FTP hosting =====================================================

#=== func check ip 100 times ===================================================
def findFTPHosting():
	""" loop to find hosting FTP """
	global MAX_TIME
	for i in xrange(0,MAX_TIME):
		ip = getIp()
		checkFTP(ip)
#=== end check ip 100 times ====================================================

#=== func start crawler ========================================================
def startCrawlerFTP():
	""" multi thread crawler """
	for i in xrange(0,MAX_THREAD):
		t = Thread(target=findFTPHosting)
		t.start()
#=== end start crawler =========================================================

startCrawlerFTP()