#Multiples

for i in range(1, 1000, 2):
    print(i)

max = 1000000

for i in range(5, max):
	if i%5 == 0:
    	print(i)

#Sum List
a = [1, 2, 5, 10, 255, 3]

b = sum(a)
print(b)

#Average List

a = [1, 2, 5, 10, 255, 3]

print(sum(a) / float(len(a)))