class node(object):
    def __init__(self,value):
        self.value=value
        self.parent=None
        self.left_child=None
        self.right_child=None
    def __str__(self):
        return str(self.value)
    def get_value(self):
        return self.value
    def get_parent(self):
        return self.parent
    def get_leftchild(self):
        return self.left_child
    def get_rightchild(self):
        return self.right_child
    def set_left_child(self,child):
        self.left_child=child
        child.set_parent(self)
    def set_right_child(self,child):
        self.right_child=child
        child.set_parent(self)
    def set_parent(self,parent):
        self.parent=parent


n5=node(5)
n2=node(2)
n1=node(1)
n4=node(4)
n8=node(8)
n7=node(7)
n6=node(6)
n3=node(3)

n5.set_left_child(n2)
#n2.set_parent(n5)
n5.set_right_child(n8)
#n8.set_parent(n5)
n2.set_left_child(n1)
#n1.set_parent(n2)
n2.set_right_child(n4)
#n4.set_parent(n2)
n4.set_left_child(n3)
#n3.set_parent(n4)
n8.set_left_child(n6)
#n6.set_parent(n8)
n6.set_right_child(n7)
#n7.set_parent(n6)


def dfs(root,key):
    """
    searches the tree using dfs to see if key is a node of the tree
    :param root:  root of the tree(node)
    :param key: value
    :return: Boolean
    """
    stack=[root]
    while len(stack)>0:
        print('At node'+str(stack[0].get_value()))
        if stack[0].value==key:
            return True
        else:
            temp=stack.pop(0)
            if temp.get_rightchild():
                stack.insert(0,temp.get_rightchild())
            if temp.get_leftchild():
                stack.insert(0,temp.get_leftchild())
    return False

def bfs(root,key):
    queue=[root]
    while len(queue)>0:
        print('At node'+str(queue[0].get_value()))
        if queue[0].get_value()==key:
            return True
        else:
            temp=queue.pop(0)
            if temp.get_leftchild():
                queue.append(temp.get_leftchild())
            if temp.get_rightchild():
                queue.append(temp.get_rightchild())
    return False
print(bfs(n5,9))
#print(dfs(n5,9))

