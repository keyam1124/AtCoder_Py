N = int(input())

prev = []
for i in range(N):
    current = []
    for j in range(i + 1):
        if j == 0 or j == i:
            current.append(1)
        else:
            current.append(prev[j - 1] + prev[j])
    print(" ".join(map(str, current)))
    prev = current
