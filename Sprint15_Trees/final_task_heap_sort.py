# Посылка 39476457

from itertools import count


class Node:
    def __init__(self, name, value, count=None):
        self.value = value
        self.name = name
        self.count = count

        self.sum = 0
        for item in self.value:
            if item > 0:
                self.sum += item

        self.kondratiy = set("kondratiy").issubset(self.name)

    def __gt__(self, other):
        if self.kondratiy:
            if other.kondratiy:
                return self.count > other.count
            return True
        if other.kondratiy:
            return False

        if self.sum != other.sum:
            return self.sum > other.sum
        if self.name != other.name:
            return (self.name < other.name)  # Если суммы равны, то первым должен идти участник, чье имя лексикографически меньше.
        return (self.count > other.count)  # Если имена одинаковые то смотрим, кто позже во входных данных

    def __str__(self):
        string = str(self.count) + " " + self.name + ": " + str(self.value)
        return string


def heap_sort(arr):
    def heapify(arr):
        start = (len(arr) - 2) // 2
        while start >= 0:
            siftdown(arr, start, len(arr) - 1)
            start -= 1

    def siftdown(arr, start, end):
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 <= end and arr[child] > arr[child + 1]:
                child += 1
            if child <= end and arr[root] > arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                return

    heapify(arr)
    end = len(arr) - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        siftdown(arr, 0, end - 1)
        end -= 1


if __name__ == "__main__":
    heap = []
    counter = count()
    with open("input.txt") as f:
        n = int(f.readline())
        for _ in range(n):
            line = f.readline().split()
            node = Node(
                name=line[0], value=list(map(int, line[1:])), count=next(counter)
            )
            heap.append(node)

    heap_sort(heap)

    for item in heap:
        print(item.name, end=" ")
        print(*item.value)
