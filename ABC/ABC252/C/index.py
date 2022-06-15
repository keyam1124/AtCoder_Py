N = int(input())
S = []

for i in range(N):
    temp = input()
    S.append(temp)

min_val = 99999999
for i in range(10):
    temp = dict()
    for j in range(N):
        index = S[j].index(f"{i}")
        if temp.get(index) is None:
            temp[index] = 1
        else:
            temp[index] += 1
    max_val = 0
    for k in temp.items():
        cnt = (k[1] - 1) * 10 + k[0]
        if cnt > max_val:
            max_val = cnt
    if min_val > max_val:
        min_val = max_val

print(min_val)
