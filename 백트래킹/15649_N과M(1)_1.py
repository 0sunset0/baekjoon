n, m = map(int, input().split())
result = [0] * (n+1)
used = [False] * (n+1)

def dfs(count):
    global n, m
    if count == m:
        for i in range(count):
            print(result[i], end=" ")
        print()
        return
    
    for i in range(1, n+1):
        if used[i] == True:
            continue
        used[i] = True
        result[count] = i
        dfs(count+1)
        used[i] = False

dfs(0)