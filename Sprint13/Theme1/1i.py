#%%
with open('input.txt') as f:
    n = f.readline().rstrip()
    massiv = f.readline().split()
massiv = list(map(int, massiv))

#%%
while len(massiv) > 1:
    massiv.sort()
    massiv.append(abs(massiv.pop() - massiv.pop()))
print(bool(1)) if massiv.pop() == 0 else print(bool(0))

# %%
