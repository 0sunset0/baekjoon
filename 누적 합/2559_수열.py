import sys


n, k = map(int, sys.stdin.readline().split())

ondo = list(map(int, sys.stdin.readline().split()))
sum_list = []
temp = 0
for i in ondo:
    temp += i
    sum_list.append(temp)
    
result = []
result.append(sum_list[k-1]) 
for i in range(0, n-k):
    result.append(sum_list[i+k]- sum_list[i])
print(max(result))