n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
result = []
used = [False] * (10001)

def dfs(count):
    if count == m:
        for i in result:
            print(i, end=" ")
        print()
        return
    
    for i in num:
        if used[i] == True:
            continue
        result.append(i)
        used[i] = True
        dfs(count+1)
        result.pop()
        used[i] = False
        
dfs(0)