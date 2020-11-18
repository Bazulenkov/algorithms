def solution(head):
    node = head
    while node.next is not None:
        node.next, node.prev = node.prev, node.next
        node = node.prev
    node.next, node.prev = node.prev, node.next
    return node