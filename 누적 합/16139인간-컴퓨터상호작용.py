import sys


s = list(sys.stdin.readline())
num = int(sys.stdin.readline())
test_case = []
for i in range(num):
    test_case.append(list(sys.stdin.readline().split()))
    
all_sum_list = []
for i in test_case:
    sum_list = [0] * (len(s)-1)
    count = 0
    for j in range(0, len(s)-1):
        if s[j] == i[0]:
            count += 1
        sum_list[j] = count
    all_sum_list.append(sum_list)
    print(sum_list)
    
    
for i in test_case:
    index = 0
    if int(i[1]) == 0:
        print(all_sum_list[index][int(i[2])])
    else:
        print(all_sum_list[index][int(i[2])] - all_sum_list[index][int(i[1])-1])
    index += 1
    
    