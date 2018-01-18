#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  n=len(tree)
  if n==0:
    return True

  keys,left,right,result=[],[],[],[]
  for i in range(n):
    keys.append(tree[i][0])
    left.append(tree[i][1])
    right.append(tree[i][2])
  #print(keys)
  #print(left)
  #print(right)

  inOrderTraverse(keys,0,left,right,result)
  for i in range(1,len(result)):
    if result[i]<=result[i-1]:
      return False

  return True


def inOrderTraverse(keys,root_index,left,right,result):
  if left[root_index]==-1 and right[root_index]==-1:
    result.append(keys[root_index])

  elif left[root_index]==-1:
    result.append(keys[root_index])
    inOrderTraverse(keys,right[root_index],left,right,result)

  elif right[root_index]==-1:
    inOrderTraverse(keys,left[root_index],left,right,result)
    result.append(keys[root_index])

  else:
    inOrderTraverse(keys,left[root_index],left,right,result)
    result.append(keys[root_index])
    inOrderTraverse(keys,right[root_index],left,right,result)





def inOrderTraverse(keys,root_index,left,right,result):
  if left[root_index]==-1 and right[root_index]==-1:
    result.append(keys[root_index])

  elif left[root_index]==-1:
    result.append(keys[root_index])
    inOrderTraverse(keys,right[root_index],left,right,result)

  elif right[root_index]==-1:
    inOrderTraverse(keys,left[root_index],left,right,result)
    result.append(keys[root_index])

  else:
    inOrderTraverse(keys,left[root_index],left,right,result)
    result.append(keys[root_index])
    inOrderTraverse(keys,right[root_index],left,right,result)


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  #print(tree)
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()

