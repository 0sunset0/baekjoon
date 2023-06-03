n = int(input())
health = [0] + list(map(int, input().split()))
joy = [0] + list(map(int, input().split()))

dp = [[0 for i in range(101)] for j in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 101):
        if health[i] <= j: #현재 체력으로 i번째 기쁨 얻기 가능
            #i번째 기쁨을 얻기 위해, i번째 체력 값을 뺀다.
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-health[i]] + joy[i])
        else: #현재 체력으로 불가능 -> 전 dp 값 그대로
            dp[i][j] = dp[i-1][j]
            
print(dp[n][99]) #100이 되면 세준이가 죽기 때문에 99까지 구한 값을 출력