class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left

def solution1(root: Node):
    stack = []
    stack.append(root)
    while stack:
        # cur_node = stack.pop()
        if stack.left:
            stack.append(stack.left)
        if stack.right:
            stack.append(stack.right)

def solution(node: Node, stack=[]):
    if not node.left and not node.right:
        return all
    stack.append(node.value)
    if node.left:
        bst = solution(node.left, stack)
        bst = all([node.left.value < item for item in stack])
        if bst == False:
            return False
        stack.pop()
    if node.right:
        bst = solution(node.right, stack)
        bst = all([node.right.value > item for item in stack])
        stack.pop()
        bst = True
    return bst
