#%%
def gcdex(a, b):
    if b == 0:
        return 1, 0, a
    x, y, d = gcdex(b, a % b)
    return y, x -y * (a // b), d

if __name__ == "__main__":
    with open("input.txt") as f:
        width = int(f.readline())
        length = int(f.readline())

    result = map(str, gcdex(width, length))
    print(' '.join(result))
# %%
