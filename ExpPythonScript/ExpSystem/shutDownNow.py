import psutil
import json
import os

LISTCLOSE 		= ['thunderbird.exe','sublime.exe','Skype.exe','explorer.exe','Taskmgr.exe','VSWinExpress.exe']

#========================================================================================================
def saveProcess(fileName):
	""" create file json to save list process """

	global LISTCLOSE

	listProc 		= psutil.process_iter()

	listProcSave 	= {}

	for item in listProc:
		try:
			if item.name() in LISTCLOSE:
				listProcSave[str(item.name())] 	= {}
				listProcSave[str(item.name())]	= {'username':item.username(), 'Path':str(item.cmdline()), 'PID': item.ppid()}
		except:
			pass

	with open(fileName,'w') as saveFile:
		json.dump(listProcSave,saveFile,indent=4,sort_keys=True,separators=(',',':'))

#========================================================================================================
def loadProcessFromFile(fileName):
	""" Load list process from json file """
	with open(fileName,'r') as loadFile:
		return json.load(loadFile)

#=======================================================================================================
def killListProcessInFile():
	""" Kill processes in file """
	global LISTCLOSE

	listProc 		= psutil.process_iter()

	for item in listProc:
		try:
			if item.name() in LISTCLOSE:
				item.kill()
		except:
			pass

	os.system('shutdown /f /s /t 7')
#=======================================================================================================
def main():
	saveProcess('saveListProcess.json')
	killListProcessInFile()

	

if __name__ == '__main__':
	main()