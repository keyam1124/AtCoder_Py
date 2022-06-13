N, K = map(int, input().split())
a = list(map(int, input().split()))

for i in range(K):
    b = []
    for j in range(i, N, K):
        b.append(a[i])
    b.sort()
    for j in range(i, N, K):
        a[i] = b[i // K]

tmp = a.copy()
tmp.sort()
print(a)
print(tmp)
for i in range(len(a)):
    if a[i] != tmp[i]:
        print("No")
        exit()
print("Yes")
