N = int(input())

ans = 1
for i in range(N):
    A = list(map(int, input().split()))
    ans *= sum(A) % 1000000007
print(ans % 1000000007)
