from collections import deque


n, k = map(int, input().split())
queue = deque()
visited = [False] * 100001

def bfs(start):
    visited[start] = True
    queue.append([start, 0])
    
    while queue:
        x, count = queue.popleft()
        if x == k:
            print(count)
            break
        if (2*x) <= 100000 and visited[2*x] == False:
            visited[2*x] = True
            queue.appendleft([2*x, count]) # 순간이동 하는 경우는 최우선으로 생각하여 큐 맨 앞에 넣는다.
        if (x+1) <= 100000 and visited[x+1] == False:
            visited[x+1] = True
            queue.append([x+1, count+1])
        if (x-1) >= 0 and visited[x-1] == False:
            visited[x-1] = True
            queue.append([x-1, count+1])
        
bfs(n)
    
