#%%
with open('input.txt') as f:
    k = int(f.readline().rstrip())
    n = int(f.readline().rstrip())
    coins = list(map(int, f.readline().split()))

def search(groups):
    if not coins:
        check = True
        for item in groups:
            check = check and bool(item == target)
        return check
    v = coins.pop()
    i = 0
    while i in range(len(groups)):
        if groups[i] + v <= target:
            groups[i] += v
            return search(groups)
        i += 1
    return False
        
#%%
coins.sort() 
s = sum(coins)
target = s // k
if s % k == 0 and k <= n and coins[-1] <= target :
    groups = [0 for item in range(k)]
    print(search(groups))
else:
    print(False)
# %%
