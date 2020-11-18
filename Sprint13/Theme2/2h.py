#%%
with open('input.txt') as f:
    n = f.read()
n = int(n)
#%%
def generate(cur, open, close, n):
    if len(cur) == 2*n:
        print(cur)
        return
    if open < n:
        generate(cur+'(', open+1, close, n)
    if close < open:
        generate(cur+')', open, close+1, n)

generate('', 0, 0, n)
# %%
