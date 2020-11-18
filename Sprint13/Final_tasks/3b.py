# 34594233

def getmax(arr, l=0, r=None):
    """Return index of array with max element."""
    r = len(arr) - 1 if r is None else r
    index_mid_elem = (r + 1 - l) // 2 + l
    mid_elem = arr[index_mid_elem]
    if arr[l] <= mid_elem <= arr[r]:
        return r
    if arr[l] > mid_elem:
        return getmax(arr, l=l, r=index_mid_elem - 1)
    else:
        return getmax(arr, l=index_mid_elem, r=r)


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


def find_element(broken_array):
    border = getmax(broken_array)
    result = binarySearch(broken_array, k, 0, border)
    if result == -1:
        result = binarySearch(broken_array, k, border)
    return result   


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        k = int(f.readline())
        arr = list(map(int, f.readline().split()))

    result = find_element(arr)

    with open("output.txt", "w") as f:
        f.write(str(result))
