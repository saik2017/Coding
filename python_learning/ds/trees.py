#implementation of binarytrees
#DFS 1)Inorder traversal 2)Preorder traversal 3)Post order traversal 4)BFS

class Node(object):
    def __init__(self,key):
        self.key=key
        self.parent=None
        self.leftChild=None
        self.rightChild=None


    def setParent(self,node):
        self.parent=node

    def setLeftChild(self,node):
        self.leftChild=node

    def setRightChild(self,node):
        self.rightChild=node

    def getParent(self):
        return self.parent

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

def BuildTree():
    n1=Node('Les')
    n2=Node('Cathy')
    n3=Node('Alex')
    n4=Node('Frank')
    n5=Node('Sam')
    n6=Node('Nancy')
    n7=Node('Violet')
    n8=Node('Tony')
    n9=Node('Wendy')
    n1.setLeftChild(n2)
    n1.setRightChild(n5)
    n2.setParent(n1)
    n5.setParent(n1)
    n2.setLeftChild(n3)
    n3.setParent(n2)
    n2.setRightChild(n4)
    n4.setParent(n2)
    n5.setLeftChild(n6)
    n6.setParent(n5)
    n5.setRightChild(n7)
    n7.setParent(n5)
    n7.setLeftChild(n8)
    n8.setParent(n7)
    n7.setRightChild(n9)
    n9.setParent(n7)

def BfsInOrder(root):
    l=[root]
    l.append()
