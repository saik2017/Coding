#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class Node(object):
    def __init__(self,index,keys):
        self.index=index
        self.key=keys[index]


def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  n = len(tree)
  if n == 0:
      return True

  nodes=[]
  keys, left, right, result = [], [], [], []
  for i in range(n):
      keys.append(tree[i][0])
      left.append(tree[i][1])
      right.append(tree[i][2])
  inOrderTraverse(keys,0,left,right,result)
  root_position=0
  for i in range(len(result)):
      if result[i].index==0:
          root_position=i
          break
  for i in range(1,len(result)):
      if i<=root_position:
          if result[i].key<=result[i-1].key:
              return False
      if result[i].key<result[i-1].key:
          return False

  return True







def inOrderTraverse(keys,root_index,left,right,result):
  if left[root_index]==-1 and right[root_index]==-1:
    result.append(Node(root_index,keys))

  elif left[root_index]==-1:
    result.append(Node(root_index, keys))
    inOrderTraverse(keys,right[root_index],left,right,result)

  elif right[root_index]==-1:
    inOrderTraverse(keys,left[root_index],left,right,result)
    result.append(Node(root_index, keys))

  else:
    inOrderTraverse(keys,left[root_index],left,right,result)
    result.append(Node(root_index, keys))
    inOrderTraverse(keys,right[root_index],left,right,result)







def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()

