S = ""
for i in range(4):
    S += input()
    
if "2" in S and "3" in S and "R" in S and len(S)==7:
    print("Yes")
else:
    print("No")