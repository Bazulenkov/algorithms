#%%
with open('input.txt') as f:
    n, k = f.readline().split()
    massiv = f.readline().split()
massiv = list(map(int, massiv))
n = int(n) # бюджет
k = int(k)
# %%
massiv.sort()
cnt = 0

for i in range(n):
    k -= massiv[i]
    if k >= 0:
        cnt += 1
    else:
        break

print(cnt)

# %%
