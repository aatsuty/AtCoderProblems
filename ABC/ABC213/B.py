import copy

N = int(input())
A = list(map(int, input().split()))
B=copy.deepcopy(A)
list.sort(A,reverse=True)
print(B.index(A[1])+1)