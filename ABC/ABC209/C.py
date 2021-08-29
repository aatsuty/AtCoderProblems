N = int(input())
C = list(map(int, input().split()))
C = sorted(C)

answer = 1

for i in range(N):
    answer *= C[i]-i
    answer %= 10**9+7
    
print(answer)