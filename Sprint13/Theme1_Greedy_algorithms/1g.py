#%%
with open('input.txt') as f:
    n = f.readline().rstrip() # кол-во строк
    m = f.readline().rstrip() # кол-во столбцов
    matrix = [list(map(int, line.split())) for line in f]

m = int(m)
n = int(n)

# %%
def spiral(n, m, a):
    l = 0 # сдвиг по горизонтали слева
    k = 0 # сдвиг по вертикали сверху
    while k < n and l < m:
        for i in range(l, m):
            print(a[k][i])
        k += 1

        for i in range(k, n):
            print(a[i][m-1])
        m -= 1

        if k < n:
            for i in range(m-1, l-1, -1):
                print(a[n-1][i])
            n -= 1

        if l < m:
            for i in range(n-1, k-1, -1):
                print(a[i][l])
            l += 1


spiral(n, m, matrix)