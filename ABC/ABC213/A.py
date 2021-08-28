A, B = map(int, input().split())
A_2 = bin(A)
B_2 = bin(B)
A_2 = A_2[2:len(A_2)]
B_2 = B_2[2:len(B_2)]

if len(A_2)>=len(B_2):
    B_2 = "0"*(len(A_2)-len(B_2))+B_2
else:
    A_2 = "0"*(len(B_2)-len(A_2))+A_2

C_2 = ""

for i in range(len(A_2)):
    n = int(A_2[i]) + int(B_2[i])
    n %= 2
    C_2 += str(n)
    
C = int(C_2,2)

print(C)