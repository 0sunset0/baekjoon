from collections import deque
import sys


queue = deque()

n = int(sys.stdin.readline())

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if len(queue) != 0:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    else:
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)