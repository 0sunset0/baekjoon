n, m = map(int, input().split())

result = []
used = [False] * (n+1) 

def dfs(count, index):
    if index == m:
        for i in result:
            print(i, end=" ")
        print()
        return
    
    start = 1
    if len(result)>0:
        start = result[-1]
    for i in range(start, n+1):
        if used[i] == True:
            continue
        else:
            result.append(i)
            used[i] = True
            dfs(count+1)
            result.pop()
            used[i] = False
            
dfs(0)