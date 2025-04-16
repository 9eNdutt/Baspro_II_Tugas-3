A = [
    [35, 42, 13, 61, 27],
    [28, 21, 33, 52, 71],
    [19, 14, 31, 15, 17],
    [31, 21, 10, 13, 22],
    [41, 42, 43, 54, 65]
]

B = [
    [25, 44, 53, 32, 31],
    [23, 19, 18, 37, 56],
    [2, 34, 55, 32, 21],
    [20, 39, 28, 67, 70],
    [2, 1, 16, 24, 21]
]

hasil = []

for i in range(5):
    baris = []
    for j in range(5):
        total = 0
        for k in range(5):
            total += A[i][k] * B[k][j]
        baris.append(total)
    hasil.append(baris)

for row in hasil:
    print(row)