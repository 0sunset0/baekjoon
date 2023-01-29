from collections import deque


n = int(input())
a = list(map(int, input().split()))

original_card = []
for i in range(n, 0, -1):
    original_card.append(i)

result = deque()
for i in range(n-1, -1, -1):
    if a[i] == 1:
        result.append(original_card[i])
    elif a[i] == 2:
        result.insert(-1, original_card[i])
    else:
        result.appendleft(original_card[i])

result.reverse()
for i in result:
    print(i, end=" ")