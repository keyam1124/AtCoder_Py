N = int(input())

dic = dict()
ans = 0
mx = 0
for i in range(N):
    st = input().split()
    s = st[0]
    t = int(st[1])
    if dic.get(s) is None:
        dic[s] = t
        if t > mx:
            mx = t
            ans = i + 1

print(ans)
