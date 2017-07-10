import math

primeList=[]
print("Enter a Number")# Ask the user for a Number
n=input()
n=int(n) #Change the number to an integer 
for index in range (0, n+1):
    primeList.append(index) # populate a list with all numbers starting from 0 to n+1
squareRoot=math.sqrt(n) #Find the square root of n

# since the square root can be decimal,
#lets convert it to the next highest integer using the ceil function
divisorRange=math.ceil(squareRoot) 
for index in range ( 2, divisorRange): #Start with 2, till the divisorRange, increment by 1.
    # there could be numbers which are factors already, and may have been set to 0, lets ignore them.
    if primeList[index]==0:
        continue # use continue to proceed to the next loop item, without executing anything below 
    for factors in range( index*2, n, index): #Start with twice the index, increment by index
        primeList[factors]=0 # find all factors of the chosen number, set all factors to 0
    #print(primeList)

while 0 in primeList:
    primeList.remove(0) # remove all 0's

print("The primes till " + str(n) + " are:")   
print(primeList) # print the primelist
    
