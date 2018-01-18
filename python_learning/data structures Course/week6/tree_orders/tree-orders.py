# python3

import sys, threading

sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.inOrderTraverse(0,self.result)
    return self.result


  def inOrderTraverse(self,root_index,result):
      if self.left[root_index]==-1 and self.right[root_index]==-1:
          result.append(self.key[root_index])

      elif self.left[root_index]==-1:
          result.append(self.key[root_index])
          self.inOrderTraverse(self.right[root_index],result)
      elif self.right[root_index]==-1:
          self.inOrderTraverse(self.left[root_index],result)
          result.append(self.key[root_index])
      else:
        self.inOrderTraverse(self.left[root_index],result)
        result.append(self.key[root_index])
        self.inOrderTraverse(self.right[root_index],result)



  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.preOrderTraverse(0,self.result)
                
    return self.result

  def preOrderTraverse(self,root_index,result):

      if self.left[root_index]==-1 and self.right[root_index]==-1:
          result.append(self.key[root_index])

      elif self.left[root_index]==-1:
          result.append(self.key[root_index])
          self.preOrderTraverse(self.right[root_index],result)
      elif self.right[root_index]==-1:
          result.append(self.key[root_index])
          self.preOrderTraverse(self.left[root_index],result)

      else:
          result.append(self.key[root_index])
          self.preOrderTraverse(self.left[root_index],result)
          self.preOrderTraverse(self.right[root_index],result)

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.postOrderTraverse(0,self.result)
    return self.result

  def postOrderTraverse(self,root_index,result):

      if self.left[root_index] == -1 and self.right[root_index] == -1:
          result.append(self.key[root_index])

      elif self.left[root_index] == -1:
          self.postOrderTraverse(self.right[root_index], result)
          result.append(self.key[root_index])

      elif self.right[root_index] == -1:
          self.postOrderTraverse(self.left[root_index], result)
          result.append(self.key[root_index])

      else:
          self.postOrderTraverse(self.left[root_index], result)
          self.postOrderTraverse(self.right[root_index], result)
          result.append(self.key[root_index])


def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()

# Concatenting the lists while returning would cost more time.
# Instead take a empty list as argument and keep updating it.