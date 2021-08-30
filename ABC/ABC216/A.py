S = input()

X = S[0:len(S)-2]
Y = int(S[len(S)-1:len(S)])

if Y <= 2:
    print(X+"-")
    exit()
    
if Y <= 6:
    print(X)
    exit()
    
print(X+"+")