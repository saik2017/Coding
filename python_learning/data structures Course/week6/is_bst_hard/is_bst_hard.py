#!/usr/bin/python3

import sys, threading
global mini
global maxi
maxi={}
mini={}
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size




def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  n = len(tree)
  if n == 0:
      return True

  nodes=[]
  keys,left, right, result = [], [], [], []
  for i in range(n):
      keys.append(tree[i][0])
      left.append(tree[i][1])
      right.append(tree[i][2])

  dummy1=maximum(keys,0,left,right)
  dummy2=minimum(keys,0,left,right)

  return isBST(keys,0,left,right)


def isBST(keys,root_index,left,right):

  if left[root_index]==-1 and right[root_index]==-1:
    return True

  if left[root_index]==-1:
    right_min=mini[right[root_index]]
    return keys[root_index]<=right_min and isBST(keys,right[root_index],left,right)

  if right[root_index]==-1:
    left_max=maxi[left[root_index]]
    return left_max<keys[root_index] and isBST(keys,left[root_index],left,right)

  else:
    left_max=maxi[left[root_index]]
    right_min=mini[right[root_index]]

    return (left_max<keys[root_index]<=right_min) and isBST(keys,left[root_index],left,right)  and isBST(keys,right[root_index],left,right)




def maximum(keys,root_index,left,right):
  """

  :param keys:
  :param root_index:
  :param right:
  :return: the maximum value of the subtree with root at root_index
  """
  global maxi
  if left[root_index]==-1 and right[root_index]==-1:
    maxi[root_index]=keys[root_index]
    return maxi[root_index]

  elif left[root_index]==-1:
    maxi[root_index]= max(keys[root_index],maximum(keys,right[root_index],left,right))
    return maxi[root_index]

  elif right[root_index]==-1:
    maxi[root_index]= max(keys[root_index],maximum(keys,left[root_index],left,right))
    return maxi[root_index]

  else:
    maxi[root_index]= max(maximum(keys,left[root_index],left,right),keys[root_index],maximum(keys,right[root_index],left,right))
    return maxi[root_index]




def minimum(keys,root_index,left,right):
  """

  :param keys:
  :param root_index:
  :param right:
  :return: the minimum value of the subtree with root at root_index
  """
  global mini

  if left[root_index]==-1 and right[root_index]==-1:
    mini[root_index]= keys[root_index]
    return mini[root_index]

  elif left[root_index]==-1:
    mini[root_index]= min(keys[root_index],minimum(keys,right[root_index],left,right))
    return mini[root_index]

  elif right[root_index]==-1:
    mini[root_index]= min(keys[root_index],minimum(keys,left[root_index],left,right))
    return mini[root_index]

  else:
    mini[root_index]= min(minimum(keys,left[root_index],left,right),keys[root_index],minimum(keys,right[root_index],left,right))
    return mini[root_index]




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

