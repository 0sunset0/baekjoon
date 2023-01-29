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
    
    for i in range(0, n):
        result.append(num[i])
        dfs(count+1)
        result.pop()
dfs(0)