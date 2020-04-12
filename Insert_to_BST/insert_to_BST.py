# Description
# Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.

# Node:
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None 
#		  self.right = None

def insertNode(root, node):
    return insert(root, node)
    
def insert(root, node):
    if root is None:
        return node
    
    if node.val < root.val:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)
    
    return root