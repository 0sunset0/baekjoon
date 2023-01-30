import sys

n = int(sys.stdin.readline())

dp1 = [0 for i in range(41)]
dp1[1] = 1
dp1[2] = 1
dp1[3] = 2



for i in range(3, n+1):
    dp1[i] = dp1[i-1] + dp1[i-2]
print(dp1[n], n-2, sep=" ")



