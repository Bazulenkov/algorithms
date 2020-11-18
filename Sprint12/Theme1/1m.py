string = input()

any_dict = dict.fromkeys(string)
for i in string:
    c = any_dict[i] if any_dict[i] else 0
    any_dict[i] = c + 1
result = sorted(any_dict, key=lambda item: (-any_dict[item], item))
for i in result:
    print(i*any_dict[i], end='')

# %%
