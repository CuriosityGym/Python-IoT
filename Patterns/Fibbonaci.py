fibnumber=int(input("Enter Number of Numbers: "))
Fiblist=[1,1]

for i in range(2, fibnumber):
    Fiblist.append(Fiblist[i-1]+Fiblist[i-2])

print(Fiblist)
