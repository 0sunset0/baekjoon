def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    if find_parent(a) > find_parent(b):
        parent[find_parent(a)] = find_parent(b)
    else:
        parent[find_parent(b)] = find_parent(a)

n = int(input())
m = int(input())

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i
edges = []
result = 0

for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append([cost, a, b])

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union(a, b)
        result += cost
print(result)