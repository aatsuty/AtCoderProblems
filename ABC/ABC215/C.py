import itertools

S = input()
S = S.split()
K = int(S[1])
S = S[0]

# S = sorted(S)
jun = list(itertools.permutations(S))
jun = set(jun)
jun = list(jun)
jun = sorted(jun)
moji = jun[K-1]
ans = ""
for m in moji:
    ans += m
    
print(ans)