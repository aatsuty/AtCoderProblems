N, K = map(int, input().split())
C = list(map(int, input().split()))

answer = 0
for i in range(N-K+1):
    myList = C[i:i+K]
    count = len(list(set(myList)))
    answer = max([answer, count])
    
print(answer)