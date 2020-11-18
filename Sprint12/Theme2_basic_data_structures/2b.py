with open('input.txt') as f:
    n = f.readline().rstrip()
    m = f.readline().rstrip()
    input_by_row = [line.rstrip().split() for line in f]
     
n = int(n)
m = int(m)
# %%
for num in range(m):
    for row in input_by_row:
        print(row[num], end=' ')
    print('')