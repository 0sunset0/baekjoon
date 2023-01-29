import heapq
import sys

n = int(sys.stdin.readline())

pq = []
for i in range(n):
    for j in list(map(int, sys.stdin.readline().split())):
        if len(pq) < n:
            heapq.heappush(pq, j)
        else:
            if j >  pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, j)


print(pq[-n])