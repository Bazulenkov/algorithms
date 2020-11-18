from collections import deque


def solution(root):
    q = deque()
    q.append(root)
    maxitem = root.value
    while q:
        cur_node = q.popleft()
        maxitem = maxitem if maxitem > cur_node.value else cur_node.value
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return maxitem
