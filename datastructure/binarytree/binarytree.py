# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ..treenode.treenode import TreeNode

class BinaryTree:
    def __init__(self, root: "TreeNode"=None):
        self.root = root
    
    def __str__(self):
        return str(self.root)

if __name__ == "__main__":
    a = BinaryTree()
    print("succesful")