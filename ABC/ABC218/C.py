def rotate(N, map):
    sin_map = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            sin_map[i][j] = map[j][N-i-1]
    return sin_map

def slide(N, n1, n2 , map):
    sin_map = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i+n1 < 0 or i+n1 >= N or j+n2 < 0 or j+n2 >= N:
                sin_map[i][j] = 0
            else:
                sin_map[i][j] = map[i+n1][j+n2]
    return sin_map
            

N = int(input())

S_map = [[0] * N for i in range(N)]
T_map = [[0] * N for i in range(N)]

for i in range(N):
    S = input()
    for j in range(N):
        if S[j] == "#":
            S_map[i][j] = 1
for i in range(N):
    T = input()
    for j in range(N):
        if T[j] == "#":
            T_map[i][j] = 1
    
    
    
for i in range(4):
    S_map = rotate(N, S_map)
    for j in range(-N,N):
        for k in range(-N,N):
            sin_map = slide(N, j, k, S_map)
            if sin_map == T_map:
                print("Yes")
                exit()
                
                
print("No")