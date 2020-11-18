#%%
from collections import defaultdict

#%%
def dict_from_string(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    return d

def are_anagrams(a, template):
    return dict_from_string(a) == template

#%%
with open('input.txt') as f:
    string = f.readline().rstrip()
    template = f.readline().rstrip()

template = dict_from_string(template)
#%%
count = 0
len_template = len(template)
for i in range(len(string) - len_template + 1):
    if are_anagrams(string[i:i+len_template], template):
        count += 1
print(count)

# %%
