n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
used = [False] * n
result_set = set()

result = []

def dfs(count):
    if count == m:
        result_set.add(tuple(result))
        return
    for i in range(n):
        if used[i] == False:
            used[i] = True
            result.append(num[i])
            dfs(count+1)
            result.pop()
            used[i] = False
dfs(0)

result_for_print = []
for i in result_set:
    result_for_print.append(i)

for i in sorted(result_for_print):
    print(*i)