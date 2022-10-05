from queue import Queue

queue = Queue()

class LeafNotInTreeError(Exception):
    pass

class Tree:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def insertChild(self, node, value):
        if node is None:
            return Tree(value)
        if value < node.value:
            node.leftChild = self.insertChild(node.leftChild, value)
        elif value > node.value:
            node.rightChild = self.insertChild(node.rightChild, value)
        return node

    def inOrderTraversal (self, root):
        if root is not None:
            self.inOrderTraversal(root.leftChild)
            print(root.value)
            self.inOrderTraversal(root.rightChild)
        else:
            return

    def preOrderTraversal (self, root):
        if root is not None:
            print(root.value)
            self.preOrderTraversal(root.leftChild)
            self.preOrderTraversal(root.rightChild)
        else:
            return
    
    def postOrderTraversal (self, root):
        if root is not None:
            self.postOrderTraversal(root.leftChild)
            self.postOrderTraversal(root.rightChild)
            print(root.value)
        else:
            return

    def breadthFirstTraversal (self):
        print(self.value)

        if self.leftChild is not None:
            queue.put(self.leftChild)
        if self.rightChild is not None:
            queue.put(self.rightChild)
        
        while queue.empty() is False:
            queue.get().breadthFirstTraversal()

    def calculateHeight(self, node):
        if node is None:
            return 0
        else:
            leftDepth = self.calculateHeight(node.leftChild)
            rightDepth = self.calculateHeight(node.rightChild)
            return max(leftDepth, rightDepth) + 1
    
    def rootToLeafSum (self, node, leaf):
        totalSum = node.value
        if node.value == leaf:
            return leaf
        elif leaf < node.value:
            totalSum += self.rootToLeafSum(node.leftChild, leaf)
        elif leaf > node.value:
            totalSum += self.rootToLeafSum(node.rightChild, leaf)
        return totalSum

    def findLeaves(self, node):
        leaves = []
        if node is None:
            return []
        elif (node.leftChild == None) & (node.rightChild == None):
            leaves.append(node.value)
        else:
            leaves = leaves + self.findLeaves(node.leftChild)
            leaves = leaves + self.findLeaves(node.rightChild)
        return leaves


if __name__ == '__main__':
    rootNode = Tree(50)
    rootNode.insertChild(rootNode, 30)
    rootNode.insertChild(rootNode, 20)
    rootNode.insertChild(rootNode, 40)
    rootNode.insertChild(rootNode, 32)
    rootNode.insertChild(rootNode, 70)
    rootNode.insertChild(rootNode, 60)
    rootNode.insertChild(rootNode, 80)
    rootNode.insertChild(rootNode, 75)
    rootNode.insertChild(rootNode, 85)

    treeLeaves = rootNode.findLeaves(rootNode)
    while True:
        try:
            leaf = int(input("Enter a leaf: "))
            if leaf not in treeLeaves:
                raise LeafNotInTreeError()
            break
        except LeafNotInTreeError:
            print("That leaf doesn't exist in the tree!")
        except Exception as e:
            print("Please enter an integer")

    print("The sum from the root to %d is: %d" % (leaf, rootNode.rootToLeafSum(rootNode, leaf)))

