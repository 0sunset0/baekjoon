from collections import deque


n, k = map(int, input().split())
queue = deque()
for i in range(1, n+1):
    queue.append(i)
    
result = []
def delete(index):
    while len(queue)!=0:
        result.append(queue[index])
        queue.remove(queue[index])
        if len(queue) == 0:
            break
        index = index + k-1
        if index > len(queue)-1:
            index = index % len(queue)
        

delete(k-1)

print("<", end="")
for i in range(0, len(result)-1):
    print(result[i], end=", ")
print(result[-1], end="")
print(">", end="")
    
    