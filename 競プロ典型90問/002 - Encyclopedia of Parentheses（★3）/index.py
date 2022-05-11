N = int(input())

if N % 2 == 1:
    exit()

ans = []
for i in range(1 << N):
    cnt = 0
    temp = []
    for j in range(N):
        if i & 1 << j:
            temp.append("(")
            cnt += 1
        else:
            temp.append(")")
            cnt -= 1
            if cnt < 0:
                break
    if cnt == 0:
        ans.append("".join(temp))

ans.sort()
for i in ans:
    print(i)
