n = int(input())
decrease_num = []

result = []
def dfs(depth, count):
    if depth == count:
        num = ""
        for i in result:
            num+=str(i)
        decrease_num.append(int(num))
        return
    
    for i in range(0, 10):
        if len(result)==0:
            result.append(i)
            dfs(depth, count+1)
            result.pop(-1)
            continue
        else:
            if i<result[len(result)-1]:
                result.append(i)
                dfs(depth, count+1)
                result.pop(-1)
            
       


depth = 1
while len(decrease_num) < n:
    if depth>10:
        print(-1)
        exit()
    dfs(depth, 0)
    depth+=1
print(decrease_num[n-1])