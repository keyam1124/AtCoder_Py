N = int(input())
sum1 = [0 for i in range(N + 1)]
sum2 = [0 for i in range(N + 1)]

for i in range(1, N + 1):
    C, P = map(int, input().split())
    if C == 1:
        sum1[i] = sum1[i - 1] + P
        sum2[i] = sum2[i - 1]
    else:
        sum1[i] = sum1[i - 1]
        sum2[i] = sum2[i - 1] + P


Q = int(input())
for i in range(Q):
    L, R = map(int, input().split())
    A = sum1[R] - sum1[L - 1]
    B = sum2[R] - sum2[L - 1]
    print(f"{A} {B}")
