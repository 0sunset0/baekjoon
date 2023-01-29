import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

result = [-1 for i in range(n)]

result[0] = num[0]

for i in range(1, n):
    if num[i] > result[i-1]+num[i]:
        result[i] = num[i]
    else:
        result[i] = result[i-1]+num[i]
        
print(max(result))