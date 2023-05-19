from collections import deque


n, m = map(int, input().split())

s = deque()
count = 0

for i in range(n):
    s.append(input())
    
for i in range(m):
    test = input()
    if test in s:
        count += 1
    
print(count)