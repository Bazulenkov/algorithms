
def solution(arr):
    c1 = 0
    c0 = 0
    result = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            c0 += 1
        else:
            c1 += 1
        if max(c0, c1) < abs(c0-c1):
            if c0 == min(c0, c1):
                c0 = 0
            else:
                c1 = 0
        if arr[i] != arr[i-1]:
            result = min(c0, c1) if min(c0, c1) - abs(c0-c1) < max(c0, c1) else max(c0, c1)
    return result * 2           
#%%
def continuous_segment(arr):
    c1 = 0
    c0 = 0
    result = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            c0 += 1
        else:
            c1 += 1
        if c0 == c1:
            result += 2 * c0
            c0 = c1 = 0
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        array = list(map(int, f.readline().split()))

    print(continuous_segment(array))
# %%
