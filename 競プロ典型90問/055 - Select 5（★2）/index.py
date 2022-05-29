N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

for i in range(N):
    for j in range(0, i):
        for k in range(0, j):
            for l in range(0, k):
                for m in range(0, l):
                    if (((A[i] * A[j] % P) * A[k] % P) * A[l] % P) * A[m] % P == Q:
                        ans += 1
print(ans)
