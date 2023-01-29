n, m = map(int, input().split())
result = []

def dfs():
    if len(result) == m:
        for i in result:
            print(i, end=" ")
        print()
        return
    
    start = 1
    if len(result) > 0:
        start = result[-1]
    for i in range(start, n+1):
        result.append(i)
        dfs()
        result.pop()

dfs()
