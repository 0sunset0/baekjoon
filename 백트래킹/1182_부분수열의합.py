n, s = map(int, input().split())
num = list(map(int, input().split()))
count = 0

def dfs(index, result):
    if index >= n:
        return
    result += num[index]
    if result == s:
        global count
        count += 1
    dfs(index+1, result - num[index])
    dfs(index+1, result)
    
dfs(0, 0)
print(count)