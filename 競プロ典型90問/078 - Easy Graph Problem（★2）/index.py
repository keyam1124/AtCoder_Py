n, m = map(int, input().split())
memo = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    if a > b:
        memo[a - 1] += 1
    else:
        memo[b - 1] += 1
ans = sum(1 for x in memo if x == 1)
print(ans)
