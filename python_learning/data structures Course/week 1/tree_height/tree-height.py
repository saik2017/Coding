# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
        def compute_height(self):
                # Replace this code with a faster implementation
                root_index=self.parent.index(-1)
                tree=createTree(self.parent)
                root=self.parent.index(-1)
                return tree[root].get_level()

class node(object):
        def __init__(self,value):
                self.value=value
                self.parent=None
                self.children=[]

        def set_parent(self,parent):
                self.parent=parent
                parent.add_child(self)

        def add_child(self,child):
                self.children.append(child)

        def get_value(self):
                return self.value

        def get_parent(self):
                return self.parent
        def get_children(self):
                return self.children
        def __str__(self):
                return 'Node value :'+str(self.value)
        def get_level(self):
                if self.children==[]:
                        return 1
                else:
                        return (1+max(i.get_level() for i in self.children))
def createTree(l):
        treelist=list(range(len(l)))
        for i in range(len(l)):
                treelist[i]=node(i)
        for i in range(len(l)):
                if l[i]==-1:
                        continue
                else:
                        treelist[i].set_parent(treelist[l[i]])
        return treelist




def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()

""" 
l=[-1,0,4,0,3]
t=createTree(l)
for i in t:
        print(i)
        print('Parent:',i.get_parent())
        print('Children:',)
        for j in i.get_children():
                print(j,)
        print('---------------------')
for i in range(len(t)):
        if t[i].get_parent()==None:
                root=i
                break
print(t[root].get_level())
"""