#%%
from itertools import combinations
from functools import reduce

with open('input.txt') as f:
    n, numbers = [line.rstrip() for line in f]

#%%
numbers = list(map(int, numbers.split()))
result = []
# %%
comb = list(combinations(numbers, 3))
for elem in comb:
    if sum(elem) == 0 and reduce(lambda x, y: x*y, elem) > 0:
        result.append(reduce(lambda x, y: x*y, elem))
# %%
print(-1) if len(result) == 0 else print(max(result))
