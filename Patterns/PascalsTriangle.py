PascalList=[[0,1,0]] #initilise a list with the first row. You can have elements of a list as a list as well. 

numberOfRows=int(input("How Many rows in the pascal's Triangle?")) #ask the user, how many rows of the triangle they wish to have
for rowNum in range(1, numberOfRows): #start a for loop, starting from 1, because the first row has been made already
    PascalList.append([]) #append a new row as a list to the pascallist.
    PascalList[rowNum].append(0) #add a zero to the new list 
    lastRowElemcount=len(PascalList[rowNum-1]) #find out how many numbers are there in the precedding row
    for element in range (0,lastRowElemcount-1): #start a new loop which will add elements one after the other from the preceeding row
        newSum=PascalList[rowNum-1][element] + PascalList[rowNum-1][element+1] # make a sum of the nth and n-1 elements
        PascalList[rowNum].append(newSum) #append it to the new list
    PascalList[rowNum].append(0)#append a zero at the end.     
print(PascalList)#print the pascallist
    
