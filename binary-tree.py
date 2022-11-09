# You learned about nodes and links in the previous exploration. A node stores a value. Those nodes had one property on them, link, which allowed you to link a node to one other node.

# In a binary tree, each node has two links, usually called left and right, which allow each node to have two children.

# You're given a node root of a binary tree that consists of a node with two children: the parent node, its left child node, and its right child node.

# Return True if the value of the root is equal to the sum of the values of its two children. Otherwise, return False.

# For example, here's the visualization of a root node with a left child and a right child:

# This is what the class looks like that defines the binary
# tree nodes.
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right

# root is an instance of the TreeNode class
def check_tree(root):
    return root.value == root.left.value + root.right.value
