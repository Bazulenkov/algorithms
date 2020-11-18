class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left




def solution(root: Node):
    def dfs_in_order(node , path =[]):
        if node.left:
            path = dfs_in_order(node.left , path)
        
        path += [node]
        
        if node.right:
            path = dfs_in_order(node.right , path)

        return  path

    arr = dfs_in_order(root)

    if len(arr) % 2 == 0 or arr[len(arr)//2] != root: # проверяю, в середине ли списка стоит корень дерева
        return False
    
    for i in range(len(arr)//2):
        if arr[i].value != arr[-i-1].value:
            return False
        
    return True