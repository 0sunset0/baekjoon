import heapq
import sys


n = int(sys.stdin.readline())

hq = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, num)