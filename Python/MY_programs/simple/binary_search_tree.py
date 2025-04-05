class Node:
    """Node class for the Binary Search Tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """Binary Search Tree implementation."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the BST."""
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Recursively insert a value into the BST."""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        """Search for a value in the BST."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Recursively search for a value in the BST."""
        if node is None or node.value == value:
            return node is not None
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder_traversal(self):
        """Perform an in-order traversal of the BST."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Recursively perform in-order traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

def main():
    """Demonstrate the Binary Search Tree."""
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        bst.insert(value)
    
    print("In-order traversal:", bst.inorder_traversal())
    
    test_values = [40, 90]
    for value in test_values:
        found = bst.search(value)
        print(f"Value {value} {'found' if found else 'not found'} in BST.")

if __name__ == "__main__":
    main()
