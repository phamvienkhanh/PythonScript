import os
import time

start_time = time.time()
count = 0

def getDir(path,strFind):
	#listResult = []
	fileList = os.listdir(path)
	if len(path) == 3:
		path = path[0:2]
	for fname in fileList:
		try:
			global count
			count +=1
			if os.path.isdir(path + "/" + fname):
				#print (path + "/" + fname)
				getDir(os.path.abspath(path + "/" + fname),strFind)
			elif fname[:len(strFind)] == strFind:
				#if strFind in open(os.path.abspath(path + "/" + fname)).read():
				#	print (path + "/" + fname)
				print (path + "/" + fname)
		except WindowsError:
			pass

	#return listResult

#strDir = raw_input("DirSearch> ")
strFind = raw_input("StrFind> ")
#getDir(os.path.abspath(strDir),strFind)
getDir('C:/',strFind)
getDir('D:/',strFind)
getDir('E:/',strFind)

print((time.time() - start_time))
print (count)

strTmp = raw_input("press to continue..... ")