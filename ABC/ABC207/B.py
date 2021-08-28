A, B, C, D = map(int, input().split())

if B>=C*D:
    print(-1)
else:
    print(-(-A//(C*D-B)))