n=input("Please enter the number till where you need Primes: ")
n=int(n)
primes=[0,0]

for index in range(2,n):
    primes.append(index)

for testNumber in range (2,n):
    for factors in range(testNumber*2, n, testNumber):
        primes[factors]=0

while 0 in primes:
    primes.remove(0) 
        
print(primes)
    

