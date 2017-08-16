#Program 2
#Program to Generate a Triangle of 1s with its apex up.

#Something like this
#    1
#   1 1
#  1 1 1
# 1 1 1 1

numberOfRows=int(input("Enter Number of Rows: "))
myString=""

for rowNum in range(1, numberOfRows+1):
    index=numberOfRows-rowNum
    #print(index)
    myString=""    
    for columnNumSpace in range (1,index+1):
        myString=myString+" "
    for columnNum in range(0,rowNum):                                                                                    
        myString=myString+ "1 "
    print(myString)    

#------------------------------------------------#    


#----The Output of the Program is like this
    
##Enter Number of Rows: 5
##    1 
##   1 1 
##  1 1 1 
## 1 1 1 1 
##1 1 1 1 1  

