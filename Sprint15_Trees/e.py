from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return str(self.value)


def solution(root1: Node, root2: Node):
    q1, q2 = deque(), deque()
    q1.append(root1)
    q2.append(root2)
    while q1 or q2:
        cur_node1 = q1.popleft()
        cur_node2 = q2.popleft()
        if cur_node1.value != cur_node2.value:
            return False
        if cur_node1.left:
            if not cur_node2.left or cur_node1.left.value != cur_node2.left.value:
                return False
            q1.append(cur_node1.left)
            q2.append(cur_node2.left)
        if cur_node1.right:
            if not cur_node2.right or cur_node1.right.value != cur_node2.right.value:
                return False
            q1.append(cur_node1.right)
            q2.append(cur_node2.right)

    return True