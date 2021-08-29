N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

leftCount   = [0]*N
rightCount  = [0]*N

for a in A:
    leftCount[a-1]      += 1
    
for c in C:
    rightCount[B[c-1]-1]  += 1
    
count = 0
for i in range(N):
    count += leftCount[i] * rightCount[i]
    
print(count)