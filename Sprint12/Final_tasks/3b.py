#%%
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


def hasCycle(node):
    while (node.next is not None) and (node.next != node.value):
        tmp = node.next
        node.next = node.value
        node = tmp
    if node.next == node.value:
        return True
    else:
        return False


#%%
node = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
print(hasCycle(node))

# %%
