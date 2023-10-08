from Nodes import BinaryTreeBST


lst = [2,5,4,3,6,7]

tree = BinaryTreeBST(lst[0])

for i in range(1, len(lst)):
    tree.insert(lst[i])

def WidthTraversal(tree):
    pass