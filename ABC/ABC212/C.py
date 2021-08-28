def getDiff(a, b):
    return abs(a-b)

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)



ans_min = 10**9


a_ind = 0
b_ind = 0
for i in range(N+M):
    ans_min = min(ans_min,getDiff(A[a_ind],B[b_ind]))
    if a_ind==N-1 or b_ind ==M-1:
        break
    if A[a_ind+1] <= B[b_ind+1]:
        a_ind += 1
    else:
        b_ind += 1

ans_min = min(ans_min,getDiff(A[N-1],B[M-1]))

print(ans_min)
