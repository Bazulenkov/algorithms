from collections import deque


class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left


def solution(root: Node):
    q = deque()
    q.append(root)
    result = [root.value]
    level = []
    cnt = 0
    n = 1
    while q:
        cur_node = q.popleft()
        if cur_node.left:
            q.append(cur_node.left)
            level.append(cur_node.left.value)
        if cur_node.right:
            q.append(cur_node.right)
            level.append(cur_node.right.value)
        cnt += 2
        if level and (cnt == 2 ** n or not q):
            result.append(level[0])
            level = []
            cnt = 0
            n += 1
    return result