import math

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) //2
        guess = list[mid]
        if 2**guess <= item and 2**(guess+1) > item:
            return mid
        if 2**guess > item:
            high = mid -1
        else:
            low = mid + 1
    return None




N = int(input())
my_list = range(0,int(math.log2(10**20)))
answer = binary_search(my_list, N)





print(answer)