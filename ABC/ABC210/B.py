N = int(input())
S = input()
for i in range(N):
    if int(S[i]):
        print(["Takahashi","Aoki"][i%2])
        break