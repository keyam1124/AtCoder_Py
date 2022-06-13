abc = list(map(int, input().split()))
b = abc[1]
abc.sort()

print("Yes" if abc[1] == b else "No")
