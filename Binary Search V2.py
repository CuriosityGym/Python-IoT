sortedList=[12,14,18,25,35,67,98,123,145,167,189,200, 400, 800, 1200, 15000]

listLength=len(sortedList)
LowerIndex=0
HigherIndex=listLength-1


print ("Please Enter the number to search for")
ItemSought=int(input())
print(sortedList)
SearchFailed = True
    
numberFound=False
while (not numberFound and LowerIndex <= HigherIndex):
    totalElements=LowerIndex + HigherIndex
    if(totalElements%2==1):        
        Midpoint= int((totalElements+1)/ 2)
    else:
        Midpoint= int((totalElements/2)+1)       
    
    if (sortedList[Midpoint] == ItemSought):
        ItemFound=True
        SearchFailed = False
        itemIndex=Midpoint
        print("Item Found at Index: " + str(Midpoint))
        break
    else:
        print("LowerIndex is:" +str(LowerIndex) + " and Higher Index is: " +str(HigherIndex))
        if (LowerIndex >= HigherIndex):
            if (sortedList[LowerIndex] == ItemSought):
                SearchFailed = False
                print("Item Found at Index: " + str(LowerIndex))
                break
            elif (sortedList[HigherIndex] == ItemSought ):
                SearchFailed = False
                print("Item Found at Index: " + str(LowerIndex))
                break
            else:    
                SearchFailed = True
                print("Element Not Found in List")
                break
        else:
            if (sortedList[Midpoint] > ItemSought):
                HigherIndex = Midpoint - 1
            else:
                LowerIndex = Midpoint + 1
                
if(SearchFailed == True):           
    print("Element Not Found in List")       
            
    
    
