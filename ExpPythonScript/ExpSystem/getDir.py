import os

def getDir(path):
	#listResult = []
	fileList = os.listdir(path)
	for fname in fileList:
		if os.path.isdir(path + "/" + fname):
			print (path + "/" + fname)
			getDir(os.path.abspath(path + "/" + fname))
		#elif fname[-len(typeFile):] == typeFile:
			#if strFind in open(os.path.abspath(path + "/" + fname)).read():
				#print (path + "/" + fname)

	#return listResult

strDir = raw_input("DirSearch> ")
#strFind = raw_input("StrFind> ")
getDir(os.path.abspath(strDir))

strDir = raw_input("press to continue..... ")