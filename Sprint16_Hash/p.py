#%%
def set_dict(keys, values):
    result = {key:"None" for key in keys}
    i = 0
    for key in keys:
        if i <= len(values) - 1:
            result[key] = values[i]
            i += 1
        else: break
    return result

if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        keys = f.readline().split()
        m = int(f.readline())
        values = f.readline().split()

    for key, value in set_dict(keys, values).items():
        print(key + ": " + value)
# %%
