import re

with open("ListFTPHost.txt","r") as fileContent:
	content = fileContent.read()
	listIP = re.findall(r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}',content)
	print(listIP)