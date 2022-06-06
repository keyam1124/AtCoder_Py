N, M = map(int, input().split())

dic = {}
for i in range(M):
    a, b = input().split()
    a_num = int(a)
    b_num = int(b)
    if a_num > b_num:
        if dic.get(a) is None:
            dic[a] = 1
        else:
            dic[a] += 1
    else:
        if dic.get(b) is None:
            dic[b] = 1
        else:
            dic[b] += 1

ans = filter(lambda x: dic[x] == 1, dic)
print(len(list(ans)))
