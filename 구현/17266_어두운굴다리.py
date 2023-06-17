n = int(input())
m = int(input())
streetlamp = list(map(int, input().split()))
result = 0

if m == 1:
    print(max(streetlamp[0], n - streetlamp[0]))
    exit()
else:
    # 가로등 사이에 어두운 공간이 없는가?
    for i in range(0, m-1):
        if (streetlamp[i+1] - streetlamp[i]) %2 != 0:
            result = max(result, (streetlamp[i+1] - streetlamp[i])//2 + 1)
        else:
            result = max(result, (streetlamp[i+1] - streetlamp[i])//2)

# 끝 가로등~ 굴다리 사이의 어두운 공간이 없는가?
result = max(result, streetlamp[0])
result = max(result, n-streetlamp[-1])
    
print(result)