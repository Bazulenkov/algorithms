#%%
def relative_sort(array, template):
    temp_arr = [0 for _ in range(len(template))]
    not_temp_arr = list()
    while array:
        added = False
        item = array.pop()
        for i in range(len(template)):
            if item == template[i]:
                temp_arr[i] += 1
                added = True
        if not added:
            not_temp_arr.append(item)
    
    not_temp_arr.sort()

    sorted_nums = list()
    for i in range(len(temp_arr)):
        for _ in range(temp_arr[i]):
            sorted_nums.append(template[i])
    return sorted_nums + not_temp_arr
    


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        arr1 = list(map(int, f.readline().split())) if n else list()
        m = int(f.readline())
        template = list(map(int, f.readline().split())) if m else list()
    
    print(*relative_sort(arr1, template))
# %%
