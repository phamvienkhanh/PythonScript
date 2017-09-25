import subprocess

def excuteCommand():
	#cmd 	= raw_input('|==|> ')
	proc 	= subprocess.Popen('start cmd.exe ',stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
	print 	'=========================================================='
	out 	= proc.stdin + proc.stderr.read()
	print 	out

while 1:
	excuteCommand()