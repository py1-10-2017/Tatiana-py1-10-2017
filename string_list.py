
#Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"

print(words.find("day"))

new_words = words.replace("day", "month")
print(new_words)

#Min and Max
x = [2,54,-2,7,12,98]

print(max(x))
print(min(x))

#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
first = x[0:1]
length = len(x)
last = x[length - 1:]

print(first + last)

#New List
list = [19,2,54,-2,7,12,98,32,10,-3,6]

list.sort()

a = list[0:5]
b = list[6:len(list)-1]
print(a)
print(b)

b.insert(0, a)
print(b)