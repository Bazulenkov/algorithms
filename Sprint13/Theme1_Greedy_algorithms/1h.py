#%%
with open('input.txt') as f:
    n = f.readline().rstrip()
    massiv = f.readline().split()
massiv = list(map(int, massiv))

def func(massiv):
    cnt = 0
    result = 0
    for i in range(len(massiv)-1, -1, -1):
        if massiv[i] > massiv[i-1]:
            cnt += 1
        else:
            if result < cnt+1:
                result = cnt+1
            cnt = 0
    print(result)

func(massiv)


# %%
