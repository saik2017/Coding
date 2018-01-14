#implementation of stack
#API methods: 1)push(key) 2)Top() 3)Pop() 4) isEmpty()
# Can Be implemented either using an array or using a linked list with push front for push.

from linkedList import LinkedList



class Stack(object):
    def __init__(self):
        self.l=[]

    def Push(self,key):
        self.l.append(key)

    def  Top(self):
        return self.l[-1]

    def Pop(self):
        return self.l.pop()

    def isEmpty(self):
        return self.l==[]

class Stack2(object):
    def __init__(self):
        self.L=LinkedList()

    def Push(self,key):
        self.L.PushFront(key)

    def Top(self):
        return self.L.TopFront()

    def Pop(self):
        self.L.PopFront()

    def isEmpty(self):
        return self.L.isEmpty()

def test():
    l1=Stack()
    l2=Stack2()
    l1.Push('a')
    l1.Push('c')
    print(l1.Top())
    l1.Pop()
    print(l1.isEmpty())
    print(l1.Top())
    l1.Pop()
    l2.Push('b')
    l2.Push('d')
    print(l2.Top())
    l2.Pop()
    print(l2.isEmpty())
    print(l2.Top())
    l2.Pop()
    print(l2.isEmpty())

#test()
