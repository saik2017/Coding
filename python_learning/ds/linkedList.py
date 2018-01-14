#python3
#Implementation of Linked list using python
#API 1)PushFront(key) 2)TopFront() 3)PopFront(key) 4)PushBack(key) 5)TopBack() 6)PopBack() 7)IsKey(key)

class Node(object):
    def __init__(self,key):
        self.key=key
        self.next=None
        self.previous=None

    def addNext(self,node):
        self.next=node

    def addPrevious(self,node):
        self.previous=node

    def changeKey(self,key):
        self.key=key

    def getKeyValue(self):
        return self.key
    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def __str__(self):
        return 'The node with value  '+str(self.key)



class LinkedList(object):
    def __init__(self):
        self.head=None
        self.tail=None

    def isEmpty(self):
        return self.head==None


    def PushFront(self,key):
        """
        Adds a node at the beginning of the list and updates the head pointer
        :param key: value of the node to be added
        Run time: O(1)
        """
        node = Node(key)
        if self.head==None:
            self.head=node
            self.tail=node

        else:
            node.addNext(self.head)
            self.head.addPrevious(node)
            self.head=node


    def TopFront(self):
        """
        run time:O(1)

        """
        if self.head==None:
            raise Exception("Empty list")
        return self.head

    def PopFront(self):
        """
        removes the node at the beginning of the list and updates the head pointer
        :return: The top or beginning node of the list
        run time:O(1)
        """
        if self.head==None:
            raise Exception("Empty list")

        node1=self.head
        if node1==self.tail:
            self.tail=None
            self.head=None
        else:
            node2=node1.getNext()
            self.head=node2
            node2.addPrevious(None)
        return node1

    def PushBack(self,key):
        """
        Adds a node with given key value at the end of the list and updates the tail pointer
        :param key: value of the node to be added.

        run time: O(1) if we for a list with tail pointer else O(n)
        """

        node = Node(key)
        if self.tail==None:
            self.head=node
            self.tail=node
        else:
            self.tail.addNext(node)
            node.addPrevious(self.tail)
            self.tail=node

    def TopBack(self):
        """

        run time: O(1) for a list with tail pointer else O(n)
        """
        if self.tail==None:
            raise Exception("Empty list")
        return self.tail

    def PopBack(self):
        """

        run time:O(1) for a list with tail pointer else O(n)
        """
        node1=self.tail
        if node1==self.head:
            self.head=None
            self.tail=None
        else:
            node2=node1.getPrevious()
            node2.addNext(None)
            self.tail=node2
        return node1

    def find(self,key):
        """

        :param key: the value of the node being searched.
        run time:O(n)
        """
        node=self.head
        while node.getNext()!=None:
            if node.getKeyValue()==key:
                return True
            else:
                node=node.getNext()
        return node.getKeyValue()==key

    def remove(self,key):
        """
        removes the first element in the linked list having the key value=key
        :param key: value
        run time: O(n) but can be O(1) if we do it by adding and removing nodes instead of values.
        """
        if self.find(key)==False:
            raise Exception("Key not in the list")
        node=self.head
        while node.getNext()!=None:
            if node.getKeyValue()==key:
                break
            else:
                node=node.getNext()
        node1=node.getPrevious()
        node2=node.getNext()
        node1.addNext(node2)
        node2.addPrevious(node1)

    def addBefore(self,nodeValue,key):
        """
        Adds a node with value key in front of first node with value nodeValue.
        :param nodeValue: value of the node succeeding the node to be added.
        :param key: value of the node to be added
        run time: O(n) but can be O(1) if we add and remove by using nodes instead of values
        """

        if self.find(nodeValue)==False:
            raise Exception("Node not in list")
        else:
            node=self.head
            while node.getKeyValue()!=nodeValue:
                node=node.getNext()
            node1=Node(key)
            node2=node.getPrevious()
            node.addPrevious(node1)
            node1.addNext(node)
            if node2==None:
                node1.addPrevious(None)
                self.head=node1
            else:
                node1.addPrevious(node2)
                node2.addNext(node1)




    def printList(self):
        """
        method to print the linked list for debugging purpose
        :return: linked list in form of a list
        """
        l=[]
        if self.head==None:
            return []
        node=self.head
        while node.getNext()!=None:
            l.append(node.getKeyValue())
            node=node.getNext()
        l.append(node.getKeyValue())
        print(l)

def test():
    L=LinkedList()
    #L.PopFront()
    #L.PushFront('a')
    L.PushBack('b')
    L.PushFront('c')
    L.PopBack()
    L.printList()
    L.PushBack('d')
    L.PopFront()
    L.printList()
    L.PushFront('e')
    L.PushBack('f')
    print(L.find('h'))
    L.PushBack('a')
    L.printList()
    L.addBefore('e','k')
    L.printList()
#test()
# Whether to add elements as nodes or values depends on the usage?



