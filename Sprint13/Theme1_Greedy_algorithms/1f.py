#%%
with open('input.txt') as f:
    n = f.readline().rstrip() # кол-во строк
    m = f.readline().rstrip() # длина строки
    lst = [line.rstrip() for line in f]

m = int(m)
n = int(n)
# %%
new_lst = []
cnt = 0
for i in range(m):
    for j in lst:
        if len(new_lst)>0 and j[i] < new_lst[-1]:
            cnt += 1
            break
        new_lst.append(j[i])
    new_lst = []
print(cnt)
