n = int(input())

a = list(map(int, input().split()))
x = int(input())

x_divisor = []
for i in range(2, x+1):
    if x%i == 0:
        x_divisor.append(i)

result = [] 
for i in a:
    flag = False
    for j in x_divisor:
        if i%j == 0:
            flag = True
    if flag == False:
        result.append(i)
print(sum(result)/len(result))