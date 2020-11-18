#%%
with open('input.txt') as f:
    n = f.readline().rstrip() # кол-во детей
    greeds = f.readline().split() # жадность каждого ребенка
    m = f.readline().rstrip() # кол-во печенек
    sizes = f.readline().split() # размеры печенек

greeds = list(map(int, greeds))
sizes = list(map(int, sizes))

greeds.sort()
sizes.sort(reverse=True)

# %%
cnt = 0

for kid in greeds:
    while sizes:
        if kid <= sizes.pop():
            cnt += 1
            break
print(cnt)
