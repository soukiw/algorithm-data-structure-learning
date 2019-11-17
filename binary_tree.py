# coding: utf-8
# Your code here!

class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None
        
    
def preorder(node):
    if node == None:
        return
    print(node.label)
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.label)
    inorder(node.right)
    
def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.label)
    
root = Node('A')
root.left = Node('B')
root.right = Node('H')
root.left.left=Node('C')
root.left.right =Node('D')
root.left.right.left=Node('E')
root.left.right.right=Node('F')
root.left.right.left.left=Node('G')

print('preorder...')
preorder(root)
print()
print('inorder...')
inorder(root)
print()
print('postorder...')
postorder(root)
    
