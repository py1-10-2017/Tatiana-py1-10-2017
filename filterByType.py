sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']


def filter(object):
	if (isinstance(object, int)):
	    if (object >= 100):
	        print "That's a big number!"
	    else:
	        print "That's a small number."

	elif (isinstance(object, str)):
	    if (len(object) >= 50):
	        print "Long sentence."
	    else:
	        print "Short sentence."

	elif (isinstance(object, list)):
	    if (len(object) >= 10):
	        print "Big list!"
	    else:
	        print "Small list."

#That's a small number.
filter(sI)
#That's a big number!
filter(mI)
#That's a big number!
filter(bI)
#That's a small number.
filter(eI)
#That's a small number.
filter(spI)
#Short sentence.
filter(sS)
#Long sentence.
filter(mS)
#Long sentence.
filter(bS)
#Short sentence.
filter(eS)
#Small list.
filter(aL)
#Big list!
filter(mL)
#Big list!
filter(lL)
#Small list.
filter(eL)
#Small list.
filter(spL)        