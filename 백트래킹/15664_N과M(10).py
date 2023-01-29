n, m = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
result = []
used = [False] * n
result_set = set()
result_list = []

def dfs(count):
    if count == m:
        result_set.add(tuple(result))
        return
    start = 0
    if count>0:
        start = num.index(result[-1]) + 1
    for i in range(start, n):
        if used[i] == True:
            continue
        used[i] = True
        result.append(num[i])
        dfs(count+1)
        used[i] = False
        result.pop()
dfs(0)
for i in result_set:
    result_list.append(i)
for i in sorted(result_list):
    print(*i)