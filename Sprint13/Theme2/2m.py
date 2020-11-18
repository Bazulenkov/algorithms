#%%
def get_nod(a, b):
    if  a % b == 0:
        return b
    return get_nod(b, a % b)      


if __name__ == "__main__":
    with open("input.txt") as f:
        width = int(f.readline())
        length = int(f.readline())

    print(get_nod(width, length))
# %%
