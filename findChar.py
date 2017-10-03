word_list = ['hello','world','my','name','is','Anna']
char = set('o')
new_list = []

for word in word_list:
    if char & set(word):
    	new_list.append(word)
    	
print new_list