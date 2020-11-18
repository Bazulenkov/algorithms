def solution(node, index):
    if index == 0:
        head = node.next_item
        return head
    else:
        head = node
    while index-1:
        if node.next_item is not None:
            node = node.next_item
        else:
            return head
        index -= 1
    node.next_item = node.next_item.next_item
    return head
    