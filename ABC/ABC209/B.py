N, X = map(int, input().split())
A = list(map(int, input().split()))
print(["No","Yes"][X>=sum(A)-N//2])