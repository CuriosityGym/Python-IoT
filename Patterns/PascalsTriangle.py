PascalList=[[0,1,0]]

numberOfRows=int(input("How Many rows in the pascal's Triangle?"))
for rowNum in range(1, numberOfRows):
    PascalList.append([])
    PascalList[rowNum].append(0)
    lastRowElemcount=len(PascalList[rowNum-1])
    for element in range (0,lastRowElemcount-1):
        newSum=PascalList[rowNum-1][element] + PascalList[rowNum-1][element+1]
        PascalList[rowNum].append(newSum)
    PascalList[rowNum].append(0)    
print(PascalList)
    
