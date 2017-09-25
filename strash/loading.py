import os, time
def animation():
	space 	= 0
	flag 	= True

	while 1:
		if flag:
			print(" "*space + "==>>")
		else:
			print(" "*space + "<<==")

		time.sleep(0.05)
		os.system("cls")
		if space < 55 and flag:
			space += 1
		else:
			flag = False

		if (not flag) and space > 0:
			space -= 1
		else:
			flag = True

class counter(object):
	print "Starting program."

	print "Loading   ",
	time.sleep(1) #do some work here...
	print "\rLoading.  ",
	time.sleep(1) #do some more work here...
	print "\rLoading.. ",
	time.sleep(1) #do even more work...
	print "\rLoading...",
	time.sleep(1) #gratuitious amounts of work...
	print "\rLoading   ",

counter()

