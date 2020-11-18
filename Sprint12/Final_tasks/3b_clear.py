# Посылка 33755008
def hasCycle(node):
    while (node.next is not None) and (node.next != node.value):
        tmp = node.next
        node.next = node.value
        node = tmp
    if node.next == node.value:
        return True
    else:
        return False
