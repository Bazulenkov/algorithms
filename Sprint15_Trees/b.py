class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left


def solution(node: Node):
    def dfs_post_order(node: Node):
        h_left = 0
        h_right = 0
        balanced=True

        if node.left:
            balanced, h_left = dfs_post_order(node.left)
        if node.right:
            balanced, h_right = dfs_post_order(node.right)

        if abs(h_right - h_left) > 1:
            balanced = False

        return balanced, max(h_left, h_right) + 1

    balanced, height = dfs_post_order(node)

    return balanced