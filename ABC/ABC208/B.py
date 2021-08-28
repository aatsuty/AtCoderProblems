N = int(input())

cnt = 0
left = N
n = 1

while left > 0:
    cnt += left % n
    left //= n
    n += 1

print(cnt)