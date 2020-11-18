#%%
def sqrt(n):
    if n == 0:
        return 1
    return (sqrt(n-1) / 2) + (1 / sqrt(n-1))

print(round(sqrt(4), 5))
# %%
