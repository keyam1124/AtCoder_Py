N, Q = map(int, input().split())
A = list(map(int, input().split()))


items = [0]
abs_sum = 0
for i in range(N - 1):
    items.append(A[i] - A[i + 1])
    abs_sum += abs(A[i] - A[i + 1])

for i in range(Q):
    L, R, V = map(int, input().split())
    if L > 1:
        temp = items[L - 1]
        items[L - 1] -= V
        abs_sum += abs(items[L - 1]) - abs(temp)
    if R < N:
        temp = items[R]
        items[R] += V
        abs_sum += abs(items[R]) - abs(temp)
    print(abs_sum)
