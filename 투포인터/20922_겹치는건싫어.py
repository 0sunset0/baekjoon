import sys


n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
count = [0] * 100001
result = 0

start = 0
end = 0
while start<=end and end < n:
    if count[num[end]] < k:
        result = max(result, end-start+1)
        count[num[end]] += 1
        end += 1
    else:
        count[num[start]] -= 1
        start += 1
    
    
print(result)