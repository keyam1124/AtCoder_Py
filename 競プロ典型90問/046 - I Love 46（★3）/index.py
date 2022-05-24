def create_mod_dic(arr):
    dic = dict()
    for item in arr:
        mod = int(item) % 46
        if dic.get(mod) is None:
            dic[mod] = 1
        else:
            dic[mod] += 1
    return dic


N = int(input())
A = create_mod_dic(input().split())
B = create_mod_dic(input().split())
C = create_mod_dic(input().split())

ans = 0
for a in A.items():
    for b in B.items():
        for c in C.items():
            if (a[0] + b[0] + c[0]) % 46 == 0:
                ans += a[1] * b[1] * c[1]

print(ans)
