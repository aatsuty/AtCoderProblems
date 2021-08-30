N = int(input())
S = []
for i in range(N):
    S.append(input())

if len(list(set(S))) != N:
    print("Yes")
else:
    print("No")    
    
