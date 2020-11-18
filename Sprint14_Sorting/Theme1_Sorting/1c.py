#%%
def effective_quiqsort(array, left, right):
    if right - left < 1:
        return
    pivot = left
    position = right
    while pivot != position:
        if pivot < position:
            if array[pivot] >= array[position]:
                array[pivot], array[position] = array[position], array[pivot]
                pivot, position = position, pivot + 1
            else:
                position -= 1
        else:
            if array[pivot] < array[position]:
                array[pivot], array[position] = array[position], array[pivot]
                pivot, position = position, pivot - 1
            else:
                position += 1
                
    effective_quiqsort(array, left, pivot-1)
    effective_quiqsort(array, pivot+1, right)
    return



if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))

    effective_quiqsort(arr, 0, len(arr)-1)
    print(*arr)
# %%
