#=== import ===================================================================
import json
#=== end import ===============================================================

#=== class person =============================================================
class person:
	def __init__(self,name,old,phone,address,email,sex):
		self.__name 	= name
		self.__old 		= old
		self.__phone 	= phone
		self.__email 	= email
		self.__sex 		= sex
		self.__address 	= address

	def getDict(self):
		result = {"Name":self.__name,"Age":self.__old,"Phone":self.__phone,"Email":self.__email,"Sex":self.__sex,"Address":self.__address}
		return result

#=== end class person =========================================================

#== init list exp =============================================================
listPerson = []
for i in xrange(0,17):
	listPerson.append(person(name="keithPham " + str(i),old=100,phone="0123456788",email="phamvienkhanh@gmail.com",address="CM",sex=1))
#==============================================================================

#=== func dump json ===========================================================
def dumpJson(sourceDict,fileDump):
	dictDump = {}
	dictDump["typeList"] = str(type(sourceDict[0]))
	dictDump["list"]	 = []
	for item in sourceDict:
		dictDump["list"].append(item.getDict())

	with open(fileDump,'w') as fileOut:
		json.dump(dictDump,fileOut,indent=4,sort_keys=True,separators=(',',':'))
#==============================================================================

#=== func main ================================================================
def Main():
	global listPerson
	dumpJson(listPerson,"ExpJson.json")
#==============================================================================

if __name__ == "__main__":
	Main()