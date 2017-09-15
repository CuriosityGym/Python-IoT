Numbers_List=[1,2,3,4,5,6,7,8,9]
number_to_Search=4
sumFound=False

LowIndex=0;
HighIndex=len(Numbers_List)-1

while(LowIndex<HighIndex):
   
    if(Numbers_List[LowIndex]+Numbers_List[HighIndex]>number_to_Search):        
        HighIndex=HighIndex-1
    elif(Numbers_List[LowIndex]+Numbers_List[HighIndex]<number_to_Search):
        LowIndex=LowIndex+1
    elif(Numbers_List[LowIndex]+Numbers_List[HighIndex]==number_to_Search):        
        print("Sum Exists")
        sumFound=True
        print(Numbers_List[LowIndex])
        print(Numbers_List[HighIndex])
        break

if( not sumFound):
    print("Sum Does Not Exist")
