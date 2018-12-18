print("Hello World")

# The basics
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

# List Combining

list1 = [1,3,5,7]
list2 = [2,4,6,8]

print(list1 + list2)

# String fun
mystring = "Hello World, I am a string!"

print(mystring[:4])
print(mystring[4:])
print(mystring[2:5])
print(mystring[-4:])
print(mystring[::2]) # skip every second character
print(mystring[::-1]) # reverse