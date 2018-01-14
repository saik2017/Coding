from linkedList import LinkedList
#API Methods: 1) Enqueue 2)Dequeue 3)isEmpty
#Note the insert method of list takes O(n) time so we cannot use it to in the Enqueue method.
# Second implementation is using a Linked list

class Queue(object):
    def __init__(self):
        self.l=[]
        self.read=0
        self.write=0

    def Enqueue(self,key):
        self.l.append(key)
        self.write+=1

    def Dequeue(self):
        temp=self.l[self.read]
        self.read+=1
        return temp

    def isEmpty(self):
        return self.read==self.write
    def size(self):
        return (self.write-self.read)


class Queue2(object):
    def __init__(self):
        self.L=LinkedList()

    def Enqueue(self,key):
        self.L.PushBack(key)

    def Dequeue(self):
         return self.L.PopFront()

    def isEmpty(self):
        return self.L.isEmpty()


def test():
    q=Queue2()
    q.Enqueue(1)
    q.Enqueue(3)
    print(q.Dequeue())
    q.Enqueue(5)
    print(q.isEmpty())
    print(q.Dequeue())
    print(q.Dequeue())
    print(q.isEmpty())


#test()

