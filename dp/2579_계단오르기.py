n = int(input())
score = []
for i in range(n):
    score.append(int(input()))

dp = [0 for i in range(300)]
dp[0] = score[0]
if n > 1:
    dp[1] = dp[0] + score[1]
if n > 2:
    dp[2] = max(score[0] + score[2], score[1] + score[2])

    for i in range(3, n):
        a = dp[i-2] + score[i]
        b = dp[i-3] + score[i] + score[i-1]
        if a >= b:
            dp[i] = a
        else:
            dp[i] = b
            
print(dp[n-1])