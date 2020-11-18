# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
with open('input.txt') as f:
    ids1, m, k, ids2 = [line.rstrip() for line in f]
# %%
k = int(k)
ids1 = list(map(int, ids1.split()[:-k]))
ids2 = list(map(int, ids2.split()))
# %%
print(" ".join(map(str, sorted(ids1 + ids2))))