list1 = [1,2,5,6,2]
list2 = [1,2,5,6,2]

list3 = [1,2,5,6,5]
list4 = [1,2,5,6,5,3]

list5 = [1,2,5,6,5,16]
list6 = [1,2,5,6,5]

list7 = ['celery','carrots','bread','milk']
list8 = ['celery','carrots','bread','cream']

def compareLists(obj1, obj2):
	if obj1 == obj2:
		print "The lists are the same"
	else:
		print "The lists are not the same." 

#same
compareLists(list1, list2)
#not the same
compareLists(list3, list4)
#not the same
compareLists(list5, list6)
#not the same
compareLists(list7, list8)