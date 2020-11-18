#%%
with open('./input.txt') as f:
    n = f.readline().rstrip()
    m = f.readline().rstrip()
    matrix = [list(map(int, line.rstrip().split())) for line in f]
    num = int(matrix.pop()[0])
    row = int(matrix.pop()[0])
n = int(n)
m = int(m)
# %%
neibors = []# %%
if 0 < row:
    neibors.append(matrix[row-1][num]) # up
if row < n-1:
    neibors.append(matrix[row+1][num]) # down
if 0 < num:
    neibors.append(matrix[row][num-1]) # left
if num < m-1:
    neibors.append(matrix[row][num+1]) # right
# %%
neibors.sort()
neibors = list(map(str, neibors))
print(' '.join(neibors))