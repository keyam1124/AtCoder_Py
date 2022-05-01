n = int(input())

ans = 1
for i in range(n):
    a = list(map(int, input().split()))
    ans *= sum(a)
    ans %= 1000000007
print(ans)
