N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_max = max(A)
indices = [i + 1 for i, x in enumerate(A) if x == a_max]
print("Yes" if len(set(B) & set(indices)) > 0 else "No")
