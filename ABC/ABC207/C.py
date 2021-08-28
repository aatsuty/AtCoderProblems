N = int(input())

l_chousei = [0,0,1,1]
r_chousei = [0,1,0,1]

l_list = []
r_list = []

for i in range(N):
    t, l, r = map(int, input().split())
    l -= l_chousei
    r += r_chousei
    l_list.append(l)
    r_list.append(r)


    
       

