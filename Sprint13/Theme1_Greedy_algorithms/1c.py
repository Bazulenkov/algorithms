#%%
with open('input.txt') as f:
    s = f.readline().rstrip() # sequence
    t = f.readline().rstrip() # string

iterator = iter(t)
print(all(elem in iterator for elem in s))



# %%
