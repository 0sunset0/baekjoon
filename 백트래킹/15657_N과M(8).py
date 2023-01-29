n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
result = []

def dfs(count):
    if count == m:
        for i in result:
            print(i, end=" ")
        print()
        return
    start = 0
    if len(result) > 0:
        start = num.index(result[-1])
    for i in range(start, n):
        result.append(num[i])
        dfs(count+1)
        result.pop()
dfs(0)