inputN, inputL = map(int, input().split())
# dp[i] = 1 (i = 0)
# dp[i] = dp[i - 1] (1 <= i < L)
# dp[i] = dp[i - 1] + dp[i - L] (i >= L)
dp = list(range(inputN + 1))
dp[0] = 1
for i in range(1, inputN + 1):
    if i < inputL:
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 1] + dp[i - inputL]

print(dp[inputN] % 1000000007)
