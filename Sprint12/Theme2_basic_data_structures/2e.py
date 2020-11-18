# class Node:  
#     def __init__(self, value, next_item=None):  
#         self.value = value  
#         self.next_item = next_item

def solution(node):
    while node.next_item is not None:
        print(node.value)
        node = node.next_item
    print(node.value)
