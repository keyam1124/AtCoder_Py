import itertools


N, W = map(int, input().split())
A = list(map(int, input().split()))
temp = set()
for i in range(1, 4):
    for j in itertools.combinations(A, i):
        a = sum(j)
        if W >= a:
            temp.add(sum(j))

print(len(temp))
