from pprint import pprint

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

print("----------")
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3
print("----------")

print("----------")
# prints out 1,2,3
for x in mylist:
    print x
print("----------")

print("------------")
pprint(mylist[::-1])
print("------------")
