class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTreeBST:
    """
    Бинарное дерево, в котором узлы упорядочены так, что для каждого узла все 
    значения в левом поддереве меньше его значения, а все значения в правом 
    поддереве больше его значения.
    """
    def __init__(self, root):
        """
        Инициализация бинарного дерева
        
        Args:
            root: Корень дерева.
        """

        if not isinstance(root, int):
            raise ValueError(f"{root} не является целым числом.")
        self.root = Node(root)

    def insert(self, data: int):
        """
        Вставка элемента в бинарное дерево
        
        Args:
            data: Значение, которое необходимо вставить.
        """
        if not isinstance(data, int):
            raise ValueError(f"{data} не является целым числом.")
        
        self._insert_recursively(self.root, data)

    def _insert_recursively(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursively(current_node.left, data)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursively(current_node.right, data)

    def search(self, data: int) -> bool:
        """
        Проверка на наличие элемента в бинарном дереве
        
        Args:
            data: Значение, которое необходимо найти.
        """
        if not isinstance(data, int):
            raise ValueError(f"{data} не является целым числом.")
        
        return self._search_recursively(self.root, data)
        
    def _search_recursively(self, current_node, data):
        if current_node is None:
            return False
        if data == current_node.data:
            return True
        elif data < current_node.data:
            return self._search_recursively(current_node.left, data)
        else:
            return self._search_recursively(current_node.right, data)

    def inorder_traversal(self) -> list:
        """
        Вывод элементов дерева.
        """
        result = []
        self._inorder_traversal_recursively(self.root, result)
        return result

    def _inorder_traversal_recursively(self, current_node, result):
        if current_node:
            self._inorder_traversal_recursively(current_node.left, result)
            result.append(current_node.data)
            self._inorder_traversal_recursively(current_node.right, result)

    def height(self) -> int:
        """
        Вывод высоты дерева.
        """
        return self._heighFind(self.root)

    def _heighFind(self, node):
        if node is None:
            return 0
        
        left_height = self._heighFind(node.left)
        right_height = self._heighFind(node.right)
        
        return max(left_height, right_height) + 1

    def isBalanced(self):
        """
        Является ли дерево сбалансированным
        """
        return self._isBalanced(self.root)

    def _isBalanced(self, root):
        if root is None:
            return True
        
        left_height = self._heighFind(root.left)
        right_height = self._heighFind(root.right)

        if abs(left_height - right_height) > 1:
            return False
        
        return self._isBalanced(root.left) and self._isBalanced(root.right)

    def reversedtree(self) -> None:
        """
        Инвертирование дерева
        """
        self._revesrsed(self.root)
    
    def _revesrsed(self, root):
        if root is None:
            return None
        
        root.left, root.right = self._revesrsed(root.right), self._revesrsed(root.left)
        
        return root
    
    # def reverseOddLevels(self):
    #     return self._reverseOddLevels(self.root)
    
    # def _reverseOddLevels(self, root):
    #     if root is None:
    #         return None
        
    #     if ((self.height()-1) - self._heighFind(root.left)) % 2 != 0:
    #         root.left, root.right = self._reverseOddLevels(root.right), self._reverseOddLevels(root.left)
    
    #     return root
    
    def binaryTreePaths(self):
        lst = []
        self._binaryTreePaths(self.root, lst)
        return lst
    
    def _binaryTreePaths(self, root, lst):
        if root is None:
            return lst
        
        left_b = self._binaryTreePaths(root.left, lst)
        lst.append(left_b)
        right_b = self._binaryTreePaths(root.right, lst)

        return root
        
    def findTilt(self):
        a = 0
        self._findTilt(self.root, a)
        return a
    
    def _findTilt(self, root, a):
        if root is None:
            return 0
        
        left_r = self._findTilt(root.left, a)
        right_r = self._findTilt(root.right, a)
        
        a += left_r - right_r
        print(a)
        return root.data





# Пример использования
root = [2,3,5]
tree = BinaryTreeBST(root[0])
for i in range(1, len(root)):
    tree.insert(root[i])

root1 = [2, 3, 5]
tree1 = BinaryTreeBST(root1[0])
for i in range(1, len(root1)):
    tree1.insert(root1[i])

print(tree.inorder_traversal())
print(tree1.inorder_traversal())

print(tree.findTilt())