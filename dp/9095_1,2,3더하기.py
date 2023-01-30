t = int(input())
dp = [-1 for k in range(12)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7
for j in range(5, 12):
    dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
for i in range(t):
    n = int(input())
    print(dp[n])