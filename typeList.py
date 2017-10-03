list1 = ['magical unicorns',19,'hello',98.98,'world']
list2 = [2,3,1,7,4,12]
list3 = ['magical','unicorns']

def typeList(object):
	sum = 0
	tempStr = " "
	intType = False
	floatType = False

	for x in object:
	    if isinstance(x, basestring):
	        tempStr = tempStr + " " + x
	    elif isinstance(x, int):
	        sum += x
	        intType = True
	    elif isinstance(x, float):
	        sum += x
	        floatType = True

	if sum != 0 and tempStr != " ":
		print "The list you entered is of mixed type"
		print tempStr
		print "Sum: " + str(sum)
	elif sum != 0 and tempStr == ' ' and intType and floatType == False:
		print "The list you entered is of integer type"
		print "Sum: " + str(sum)
	elif sum == 0 and tempStr != ' ':
		print "The list you entered is of string type"
		print "String: " + tempStr

typeList(list1)
typeList(list2)
typeList(list3)