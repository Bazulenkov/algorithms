#%%
class DoubleConnectedNode:  
    def __init__(self, value, next=None, prev=None):  
        self.value = value  
        self.next = next  
        self.prev = prev

#%%
def solution(head):
    node = head
    while node.next is not None:
        node.next, node.prev = node.prev, node.next
        node = node.prev
    node.next, node.prev = node.prev, node.next
    return node

# %%
n3 = DoubleConnectedNode('third')
n2 = DoubleConnectedNode('second', n3)
n1 = DoubleConnectedNode('first', n2)

# %%
n3 = DoubleConnectedNode('third',None, n2)
n2 = DoubleConnectedNode('second', n3, n1)
n1 = DoubleConnectedNode('first', n2)

# %%
solution(n1)