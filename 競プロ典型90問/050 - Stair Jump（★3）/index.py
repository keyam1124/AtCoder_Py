N, L = map(int, input().split())

NUM = 1000000007

dp = []
dp.append(1)
for i in range(1, N + 1):
    if i < L:
        dp.append(dp[i - 1])
    else:
        dp.append(dp[i - 1] + dp[i - L])

print(dp[N] % NUM)
