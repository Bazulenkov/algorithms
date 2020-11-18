def solution(head, value):
    node = head
    index = 0
    while node:
        if node.value == value:
            return index
        index += 1
        node = node.next_item
    return -1