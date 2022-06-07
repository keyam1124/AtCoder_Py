H, W = map(int, input().split())
A = []
B = []

for i in range(H):
    A.append(list(map(int, input().split())))
for i in range(H):
    B.append(list(map(int, input().split())))

ans = 0

for h in range(H - 1):
    for w in range(W - 1):
        a = A[h][w]
        b = B[h][w]
        diff = a - b
        if diff > 0:
            ans += diff
            A[h][w] -= diff
            A[h + 1][w] -= diff
            A[h][w + 1] -= diff
            A[h + 1][w + 1] -= diff
        elif diff < 0:
            ans -= diff
            A[h][w] -= diff
            A[h + 1][w] -= diff
            A[h][w + 1] -= diff
            A[h + 1][w + 1] -= diff
        if w == W - 2:
            if A[h][w + 1] != B[h][w + 1]:
                print("No")
                exit()
    if h == H - 2:
        if A[h + 1][w] != B[h + 1][w]:
            print("No")
            exit()

print("Yes")
print(ans)
