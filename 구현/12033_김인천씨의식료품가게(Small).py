n = int(input())

for test_case in range(n):
    result = []
    n = int(input())
    num = list(map(int, input().split()))
    for discount_index in range(len(num)):
        if num[discount_index] != 0 :
            result.append(num[discount_index])
            for original_index in range(discount_index, len(num)):
                if num[original_index]*0.75 == num[discount_index]:
                    num[original_index] = 0
                    num[discount_index] = 0
            
    print(f'Case #{test_case+1}: ', end='')
    print(' '.join(map(str, sorted(result))))