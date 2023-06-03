n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]

dp[0] = a[0]

for i in range(n):
    for j in range(i):
        if a[j] > a[i]:
            dp[i] = max(dp[i], dp[j] + a[i])
        else:
            dp[i] = max(dp[i], a[i])
print(max(dp))