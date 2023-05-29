h = int(input())
num = list(map(int, input().split()))

array= [[] for i in range(h+1)]

def solve(num, count):
    count+=1
    if len(num) == 1:
        array[count].append(num[0])
        return
    root_index = len(num)//2
    array[count].append(num[root_index])
    solve(num[:root_index], count)
    solve(num[root_index+1:], count)
    
    
solve(num, 0)


for i in range(1, len(array)):
    for j in array[i]:
        print(j, end=" ")
    print()


    