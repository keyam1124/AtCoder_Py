N = int(input())
S = input()

# ランレングス圧縮

arr = [1]
for i in range(1, len(S)):
    if S[i - 1] == S[i]:
        arr[-1] += 1
    else:
        arr.append(1)

m = (N * (N + 1)) // 2
ans = 0
for item in arr:
    ans += (item * (item + 1)) // 2
print(m - ans)
