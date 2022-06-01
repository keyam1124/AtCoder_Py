def from8to10(val):
    val_str = str(val)
    val_len = len(val_str)
    ans = 0
    for i in range(val_len):
        num = int(val_str[i])
        ans += pow(8, val_len - 1 - i) * num
    return ans


def from10to9(val):
    ans = ""
    while True:
        shou = val // 9
        amari = val % 9
        ans = f"{amari}{ans}"
        if shou >= 9:
            val = shou
        else:
            ans = f"{shou}{ans}"
            break
    return ans


N, K = map(int, input().split())

ans = N
for i in range(K):
    ans = from8to10(ans)
    ans = from10to9(ans)
    ans_str = str(ans)
    ans_str = ans_str.replace("8", "5")
    ans = int(ans_str)

print(ans)
