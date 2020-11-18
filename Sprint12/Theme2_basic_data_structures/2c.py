s = (input())
#%%
lst = []
maxlen = 0
#%%
for i in s:
    lst += i
    if len(set(lst)) != len(lst):
        if maxlen < len(lst)-1:
            maxlen = len(lst) - 1
        del lst[0]
if maxlen < len(lst):
    maxlen = len(lst)
#%%
print(maxlen)