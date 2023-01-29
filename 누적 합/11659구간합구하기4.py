n, m = map(int, input().split())
num = list(map(int, input().split()))
section = []
for i in range(m):
    section.append(list(map(int, input().split())))

sum = []
temp = 0
for i in num:
    temp += i
    sum.append(temp)

for i in section:
    result = 0
    
    if i[0] != 1:
        print(sum[i[1]-1] - sum[i[0]-2])
    else:
        print(sum[i[1]-1])