N = int(input())
S = input()

a = [0]
b = [0]
for i in range(1, N + 1):
    if S[i - 1] == "o":
        a.append(i)
        b.append(b[i - 1])
    else:
        a.append(a[i - 1])
        b.append(i)


ans = 0
for i in range(1, N + 1):
    ans += min(a[i], b[i])

print(ans)
