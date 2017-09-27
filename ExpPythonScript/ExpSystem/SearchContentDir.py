import os

def getDir(path,strFind,typeFile):
	#listResult = []
	fileList = os.listdir(path)
	for fname in fileList:
		if os.path.isdir(path + "/" + fname):
			#print (path + "/" + fname)
			getDir(os.path.abspath(path + "/" + fname),strFind,typeFile)
		elif fname[-len(typeFile):] == typeFile:
			if strFind in open(os.path.abspath(path + "/" + fname)).read():
				print (path + "\\" + fname)

	#return listResult

strDir = raw_input("DirSearch> ")
strFind = raw_input("StrFind> ")
strType = raw_input("StrType> ")
getDir(os.path.abspath(strDir),strFind,strType)

strTemp = raw_input("press to continue..........")
