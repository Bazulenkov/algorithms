#%%


def solution1(n: int):
    k1 = k2 = k3 = 1
    lst = [1]*(n+1)
    for i in range(2, n+1):
        p1, p2, p3 = lst[k1] * 2, lst[k2] * 3, lst[k3] * 5
        min_p = min(p1, p2, p3)
        lst[i] = min_p
        if min_p == p1:
            k1 += 1
        if min_p == p2:
            k2 += 1
        if min_p == p3:
            k3 += 1
        # lst.append(min_p)
    return lst[-1]

#%%
from heapq import heappop, heappush
from itertools import islice


def solution2(n: int):
    heap = [1]
    for i in range(n):
        h = heappop(heap)
        while heap and h==heap[0]:
            heappop(heap)
        for m in [2, 3, 5]:
            heappush(heap, m * h)
        yield h


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())

    print(solution1(n)) # solution1

    y = islice(solution2(n),n-1,n)
    print(*y) # solution2

# %%
