#C:/python27/
import os

if not os.path.exists('D:/DontTouchMe/tastPython'):
	os.makedirs('D:/DontTouchMe/tastPython')
filepath = os.path.join('D:/DontTouchMe/tastPython','filenew.py')
fileOut= open(filepath,'w')
file = open(__file__,'r')
str = file.read()
fileOut.write(str)
file.close()
fileOut.close()

