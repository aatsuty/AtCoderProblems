N, K = map(int, input().split())
AB = []
for i in range(N):
    AB.append(list(map(int, input().split())))
    
AB = sorted(AB, key = lambda x: x[0])

mura = 0
kane = K

for ab in AB:
    # 友人村まで到達できないとき
    if ab[0] - mura > kane:
        mura += kane
        print(mura)
        exit()
    # 友人村まで到達できるとき
    else:
        kane -= (ab[0] - mura)
        mura = ab[0]
        kane += ab[1]
        
mura += kane
print(mura)