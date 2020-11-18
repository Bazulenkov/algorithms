#%%
def count_pairs(nums, mid):
    count = 0
    j = 0
    for i in range(len(nums)):
        while j < len(nums) and abs(nums[j] - nums[i]) <= mid:
            j += 1
        count += (j - i - 1)
    return count 


def k_min_difference(arr, k):
    arr.sort()

    # low = arr[1] - arr[0]
    # for i in range(1, len(arr)-1):
    #     low = min(low, arr[i+1] - arr[i])
    low = 0

    high = arr[-1] - arr[0]

    while low < high:
        mid = (low + high) // 2 # mid = (low + high) >> 1
        if count_pairs(arr, mid) < k:
            low = mid + 1
        else:
            high = mid
    
    return low


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        array = list(map(int, f.readline().split()))
        k = int(f.readline())

    print(k_min_difference(array, k))
# %%
