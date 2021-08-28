import math

N = int(input())

my_list = []

for a in range(2, int(N**0.5)+1):
    for b in range(2, int(math.log(N,a))+1):
        my_list.append(a**b)
        
my_list = list(set(my_list))

print(N-len(my_list))