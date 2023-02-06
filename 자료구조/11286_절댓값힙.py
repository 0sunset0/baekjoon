import heapq
import sys


n = int(sys.stdin.readline())

value = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(value) == 0:
            print(0)
        else:
            absolute_value, num = heapq.heappop(value)
            print(num)
            
            
    else:
        absolute_value = num
        if num<0:
            absolute_value = -num
        heapq.heappush(value, (absolute_value, num))