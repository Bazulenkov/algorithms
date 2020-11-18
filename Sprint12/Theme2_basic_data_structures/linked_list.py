#%%
class Node:
    def __init__(self, value = None, next_item = None):
        self.value = value
        self.next_item = next_item
        
    def __str__(self):
        return self.value
#%%
def insert_node(node, index, value):
    head = node
    new_node = Node(value)
    if index == 0:
        new_node.next_item = node
        return new_node
    while index-1:
        node = node.next_item
        index -= 1
    tmp = node.next_item
    node.next_item = new_node
    new_node.next_item = tmp
    return head

#%%
def print_node(node):
    while node.next_item is not None:
        print(node.value)
        node = node.next_item
    print(node.value)

#%%
def delete_node(node, index):
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
#%%
def search_node(head, value):
    node = head
    index = 0
    while node:
        if node.value == value:
            return index
        index += 1
        node = node.next_item
    return -1

#%%
n3 = Node('third')
n2 = Node('second', n3)
n1 = Node('first', n2)

#%%
insert_node(n1, 3, 'ins')
#%%
print_node(n1)

# %%
solution(n1, 3)

# %%
n1

# %%
