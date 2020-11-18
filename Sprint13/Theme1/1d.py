#%%
with open('input.txt') as f:
    c = f.readline().rstrip() # вместимость рюкзака
    n = f.readline().rstrip() # кол-во предметов
    things = [tuple(map(int, line.split())) for line in f]
c = int(c)

sorted_things = sorted(things, key= lambda item: (-item[0], item[1]))
bag = []
for thing in sorted_things:
    if c >= thing[1]:
        bag.append(things.index(thing))
        c -= thing[1]
bag.sort()
print(*bag)

# %%
