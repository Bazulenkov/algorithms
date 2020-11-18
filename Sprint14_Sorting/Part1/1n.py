#%%
def diagonal_sort(A, n, m):
    def sort(i, j):
        vals = list()
        while i <= n - 1 and j <= m - 1:
            vals.append(A[i][j])
            i += 1
            j += 1
        vals.sort()
        while vals:
            A[i - 1][j - 1] = vals.pop()
            i -= 1
            j -= 1

    for string in range(n):
        sort(string, 0)
    for row in range(m):
        sort(0, row)


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())  # число строк
        m = int(f.readline())  # число столбцов
        matrix = [list(map(int, f.readline().split())) for _ in range(n)]

diagonal_sort(matrix, n, m)
for string in matrix:
    print(*string)
