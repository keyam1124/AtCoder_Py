n, q = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    ans += abs(a[i] - a[i + 1])

b = []
for i in range(n - 1):
    b.append(a[i] - a[i + 1])
for i in range(q):
    L, R, V = map(int, input().split())
    if L > 1:
        temp = b[L - 2]
        b[L - 2] -= V
        ans += abs(b[L - 2]) - abs(temp)
    if R < n:
        temp = b[R - 1]
        b[R - 1] += V
        ans += abs(b[R - 1]) - abs(temp)
    print(ans)
