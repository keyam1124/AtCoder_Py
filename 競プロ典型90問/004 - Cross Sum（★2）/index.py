H, W = map(int, input().split())

row_sums = [0 for i in range(H + 1)]
col_sums = [0 for i in range(W + 1)]
A = []
for y in range(1, H + 1):
    a_row = list(map(int, input().split()))
    A.append(a_row)
    row_sums[y] = sum(a_row)
    for x in range(1, len(a_row) + 1):
        col_sums[x] += a_row[x - 1]

for y in range(1, H + 1):
    b_row = []
    for x in range(1, W + 1):
        b_row.append(row_sums[y] + col_sums[x] - A[y - 1][x - 1])
    print(" ".join([str(n) for n in b_row]))
