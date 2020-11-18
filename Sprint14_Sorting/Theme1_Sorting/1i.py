#%%
def solution(array):
    pink = list()
    yellow = list()
    red = list()
    for item in array:
        if item == 0:
            pink.append(item)
        elif item == 1:
            yellow.append(item)
        else:
            red.append(item)
    return pink + yellow + red


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))

print(*solution(arr))
# %%
