import re
import string
def convertString(contents,num):
	result = ""
	for c in contents:
		if c not in (".", " ",")","("):
			if ord(c) + 2 > ord("z"):
				result += str(unichr(ord(c) - 24 + num))
			else:
				result += str(unichr(ord(c) + num))
		else:
			result += c
	return result

contents = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#print convertString("map")

#===============================================================================

def findCharacters(fileName):
	with open(fileName,"r") as Contents:
		text = Contents.read()
		strContent = re.findall(r"[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]",text)
		return strContent

#print findCharacters("source2.txt")

#for i in xrange(1,3):
#	print convertString(findCharacters("source2.txt"),i)
#	print "\n"


#===============================================================================
import urllib
uri 	= "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
def loopRequest(url,num):
	pattern = re.compile("and the next nothing is (\d+)")
	while True:
		content = urllib.urlopen(url % num).read().decode('utf-8')
		print content
		match = pattern.search(content)
		if match == None:
			break
		num = match.group(1)
loopRequest(uri,"1234")

