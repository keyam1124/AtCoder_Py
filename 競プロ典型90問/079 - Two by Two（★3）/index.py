h, w = map(int, input().split())

a = []
for i in range(h):
    a.append(list(map(int, input().split())))

b = []
for i in range(h):
    b.append(list(map(int, input().split())))

ans = 0
for y in range(h):
    for x in range(w):
        a_item = a[y][x]
        b_item = b[y][x]
        if a_item == b_item:
            continue
        if a_item > b_item:
            diff = a_item - b_item
            a[y][x] -= diff
            a[y + 1][x] -= diff
            a[y][x + 1] -= diff
            a[y + 1][x + 1] -= diff
            ans += diff
        if a_item < b_item:
            diff = b_item - a_item
            a[y][x] += diff
            a[y + 1][x] += diff
            a[y][x + 1] += diff
            a[y + 1][x + 1] += diff
            ans += diff

        if x == w - 2:
            if a[y][x + 1] != b[y][x + 1]:
                print("No")
                exit()
        if y == h - 2:
            if a[y + 1][x] != b[y + 1][x]:
                print("No")
                exit()
print("Yes")
print(ans)
