H, W = map(int, input().split())
S = []
pieces = []
for i in range(H):
    temp = input()
    piece_index1 = temp.find("o")
    if piece_index1 != -1:
        pieces.append([i, piece_index1])
        piece_index2 = temp.find("o", piece_index1 + 1)
        if piece_index2 != -1:
            pieces.append([i, piece_index2])
    S.append(temp)

distance = abs(pieces[0][0] - pieces[1][0]) + abs(pieces[0][1] - pieces[1][1])
print(distance)
