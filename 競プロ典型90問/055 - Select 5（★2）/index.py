n, p, q = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(0, n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            for L in range(k + 1, n):
                for m in range(L + 1, n):
                    if (((a[i] * a[j] % p) * a[k] % p) * a[L] % p) * a[m] % p == q:
                        ans += 1
print(ans)
