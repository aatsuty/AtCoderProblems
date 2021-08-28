import math

def getDistance(X, Y):
    return math.sqrt((X[0]-Y[0])**2 + (X[1]-Y[1])**2)

R, X, Y  = map(int, input().split())
distance = getDistance([0,0], [X,Y])
num = math.ceil(distance/R)
print(num)