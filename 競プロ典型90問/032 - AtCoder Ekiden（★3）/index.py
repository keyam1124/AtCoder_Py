import itertools


N = int(input())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))

M = int(input())
two_dim_array = [[0 for __ in range(N)] for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    two_dim_array[x - 1][y - 1] = two_dim_array[y - 1][x - 1] = 1

ans = 10**9
for item in itertools.permutations(range(N), N):
    temp = 0
    is_ng = False
    for i in range(N):
        if i < N - 1:
            if two_dim_array[item[i]][item[i + 1]] == 1:
                is_ng = True
                break
        temp += A[item[i]][i]
    if not is_ng:
        if ans > temp:
            ans = temp

print(ans if not (ans == 10**9) else -1)
