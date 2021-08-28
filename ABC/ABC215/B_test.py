import math

def printShisu(n):
    shisu = int(math.log2(n))
    print(str(n)+" "+str(shisu))


for i in range(1,10**2):
# for i in range(1,10**18):
    printShisu(i)