
class Node(object):
    def __init__(self,key):
        self.key=key
        self.parent=None
        self.leftChild=None
        self.rightChild=None

    def __str__(self):
        return str(self.key)

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

class BST(object):
    def __init__(self,root):
        self.root=root

    def find(self,node1,key):
        """

        :param node1: searches the tree rooted at node1
        :param key: the  value of the node to be searched
        :return: returns the node if found or else the position in the tree where key can be inserted.
        """
        if node1.key==key:
            return node1
        elif node1.key>key:
            if node1.getLeftChild()!=None:
                return self.find(node1.getLeftChild(),key)
            return node1

        elif node1.key<key:
            if node1.getRightChild()!=None:
                return self.find(node1.getRightChild(),key)
            return node1

    def before(self,node):
        if node.getLeftChild()==None:
            return self.leftAncestor(node)
        else:
            return self.rightDescendant(node.getLeftChild())

    def rightDescendant(self,node):
        if node.getRightChild()==None:
            return node
        else:
            return self.rightDescendant(node.getRightChild())

    def leftAncestor(self,node):
        if node.getParent()==None:
            return None
        if node.getParent().key<node.key:
            return node.getParent()
        else:
            return self.leftAncestor(node.getParent())

    def next(self,node):
        if node.getRightChild()==None:
            return self.rightAncestor(node)
        else:
            return self.leftDescendant(node.getRightChild())

    def leftDescendant(self,node):
        if node.getLeftChild()==None:
            return node
        else:
            return self.leftDescendant(node.getLeftChild())

    def rightAncestor(self,node):
        if node.getParent()==None:
            return None

        elif node.getParent().key>node.key:
            return node.getParent()
        else:
            return self.rightAncestor(node.getParent())

    def rangeSearch(self,x,y,node):
        """
        lists all nodes having values between x and y included.
        :param x: lower bound
        :param y: upper bound
        :param node: searches the tree rooted at node
        :return: list of nodes with values bounded by x and y.
        """
        l=[]
        start=self.find(node,x)
        while start.key<=y:
            if start.key>=x:
                l.append(start)
                start=self.next(start)
        return l

    def neighbors(self,node):
        return (self.before(node),self.next(node))

    def insert(self,node,key):
        """
        insert ta node with value key in the tree rooted at node
        :param node: tree with node as root
        :param key: value of the node to be inserted
        """
        position=self.find(node,key)
        if position.key==key:
            print("node already present")
        elif position.key>key:
            n=Node(key)
            position.setLeftChild(n)
            n.setParent(position)
            print(n.getParent())
        else:
            n=Node(key)
            position.setRightChild(n)
            n.setParent(position)

    def delete(self,key):
        """
        :param key: assumes key to be present in the tree.
        """
        node=self.find(self,self.root,key)
        parent=node.getParent()
        if node.getRightChild()==None:
            if parent.getRightChild()==node:
                parent.setRightChild(node.getLeftChild())
                node.getLeftChild().setParent(parent)
            else:
                parent.setLeftChild(node.getLeftChild())
                node.getLeftChild().setParent(parent)

        else:
            next=self.next(node)
            assert next.getLeftChild==None
            parent2=next.getParent()
            if parent.getRightChild()==node:
                parent.setRightChild(next)
                next.setParent(parent)
            else:
                parent.setLeftChild(next)
                next.setParent(parent)

            if parent2.getRightChild()==next:
                parent2.setRightChild(next.getRightChild())
                next.getRightChild().setParent(parent2)
            else:
                parent2.setLeftChild(next.getRightChild())
                next.getRightChild().setParent(parent2)








n1=Node(7)
n2=Node(4)
n3=Node(13)
n4=Node(1)
n5=Node(6)
n6=Node(10)
n7=Node(15)
n1.setLeftChild(n2)
n2.setParent(n1)
n1.setRightChild(n3)
n3.setParent(n1)
n2.setLeftChild(n4)
n4.setParent(n2)
n2.setRightChild(n5)
n5.setParent(n2)
n3.setLeftChild(n6)
n6.setParent(n3)
n3.setRightChild(n7)
n7.setParent(n3)
t=BST(n1)


#print(t.find(n1,5))
#print(t.rightAncestor(n7))
#print(t.next(n7))
#print(t.leftAncestor(n5))
# t=t.neighbors(n6)
# for j in t:
#     print(j)

#print(t.before(n4))
# l=t.rangeSearch(5,12,n1)
# for i in l:
#     print(i)

t.insert(n1,5)
print(n5.getLeftChild())

