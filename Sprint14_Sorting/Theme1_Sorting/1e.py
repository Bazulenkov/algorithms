#%%
def binarySearch(arr, x, l=0, r=None):
    r = len(arr) - 1 if r is None else r
    if r < l:
        return -1

    mid = l + (r - l) // 2

    if arr[mid] == x:
        return mid

    elif arr[mid] > x:
        return binarySearch(arr, x, l, mid - 1)

    else:
        return binarySearch(arr, x, mid + 1, r)


def quicksort(array):
    if len (array) < 2:
        return array # базовый случай: массивы с 0 и 1 элементом уже отсортированы
    else:
        pivot = array[0] #рекурсивный случай
        less = [i for i in array[1:] if i <= pivot] #подмассив всех элементов, меньших опорного
        greater = [i for i in array[1:] if i > pivot] #подмассив всех элементов, больших опорного
        return quicksort(less) + [pivot] + quicksort(greater)

def search(arr1, arr2):
    result = list()
    for item in arr1:
        if binarySearch(arr2, item) != -1:
            result.append(item)
            arr2.remove(item)
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        m = int(f.readline())
        arr1 = list(map(int, f.readline().split())) if n else list()
        arr2 = list(map(int, f.readline().split())) if m else list()

arr2 = quicksort(arr2)


print(*search(arr1, arr2))
# %%
