print("Hello World")

name = "joey"
age = 27

print(name + str(age))

testList = [0,1,2]
testList.append(3)
testList.append(4)

for member in testList:
    print(member)

for index,member in enumerate(testList):
    print("Index: " + str(index) + " item: " + str(member))