#%%
with open('input.txt') as f:
    n = f.read()
n = int(n)

a = 1
for i in range(1, n+1):
    a *= i

print(a)
# %%
