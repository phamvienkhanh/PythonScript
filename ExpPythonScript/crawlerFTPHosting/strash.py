
from threading import Thread
import time

COUNT = 0

def printStringOne():
	global COUNT
	for i in xrange(0,15):
		COUNT += 1
		with open("strash.txt","a") as fileOut:
			fileOut.write("threading " + str(COUNT) + "\n")

		time.sleep(2)

def printStringTwo():
	global COUNT
	for i in xrange(0,15):
		COUNT += 1
		with open("strash.txt","a") as fileOut:
			fileOut.write("threading Two " + str(COUNT) + "\n")

t1 = Thread(target=printStringOne)
t2 = Thread(target=printStringTwo)

t1.start()
t2.start()
t1.join()
t2.join()

print "end thread"