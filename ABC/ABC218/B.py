P = list(map(int, input().split()))
S = "abcdefghijklmnopqrstuvwxyz"
str = ""

for p in P:
    str += S[p-1]
    
print(str)