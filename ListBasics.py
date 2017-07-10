#Creating a List
anyListName=["a","b","c","d","e"]

#List of Numbers
numberList=[100, 200, 300, 400, 500]


#Accessing List Values by index
print(numberList[1])

# Print whole List
print(numberList)


# What is the Length of the List?
lengthOfList= len(numberList)

# Traversing through all elements and printing them
for i in range (0,lengthOfList) :
    print(numberList[i])

#OR alternativelly, if your list expands and contracts, dont find length, just use
for element in anyListName:
    print(element)

#Writing a conditional statement
if (numberList[3]==400):
   print ("The Third Number is 400")
else:
   print("The third Number is not 4")


#Add an Element to the List using append
numberList.append(10);
print(numberList)


#Delete and element in the list
del numberList[4]
print(numberList)
    
