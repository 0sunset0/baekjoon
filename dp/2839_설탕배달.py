n = int(input())

dp = [(-1) for i in range(5001)]
dp[3] = 1
dp[5] = 1
for i in range(6, n+1):
    count = list()
    if dp[i-3] != -1:
        count.append(dp[i-3]+1)
    if dp[i-5] != -1:
        count.append(dp[i-5]+1)
        
    if len(count) == 0:
        dp[i] = -1
    else:
        dp[i] = min(count)
print(dp[n])