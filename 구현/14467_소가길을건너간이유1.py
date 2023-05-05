n = int(input())
cows = [2] * 11
count = 0

for i in range(n):
    num, position = map(int, input().split())
    if cows[num] != position:
        if cows[num] == 2:
            cows[num] = position 
            continue
        count += 1
        cows[num] = position 
print(count)
    
