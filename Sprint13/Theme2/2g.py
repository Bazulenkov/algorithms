#%%
with open('input.txt') as f:
    n = f.read()

m = ord(n)
# %%
def rec(x):

    if x >= 97:
        rec(x-1)
        print(chr(x), end=' ')
    else:
        return

rec(m)
# %%
