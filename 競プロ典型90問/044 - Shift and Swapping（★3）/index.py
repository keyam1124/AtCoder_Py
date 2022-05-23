N, Q = map(int, input().split())
A = list(map(int, input().split()))

shift = 0
for i in range(Q):
    T, x, y = map(int, input().split())

    x_i = x - 1 + N - shift if x - 1 < shift else x - 1 - shift
    y_i = y - 1 + N - shift if y - 1 < shift else y - 1 - shift

    if T == 1:
        temp = A[x_i]
        A[x_i] = A[y_i]
        A[y_i] = temp
    elif T == 2:
        shift = 0 if shift == N - 1 else shift + 1
    else:
        print(A[x_i])
