N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = 0

for i in range(N):
    a = A[i]
    b = B[i]
    diff += abs(a - b)


ans = "Yes" if K >= diff and (K - diff) % 2 == 0 else "No"
print(ans)
