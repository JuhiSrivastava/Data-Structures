#!/usr/bin/python3

import sys, threading
import numpy as np

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(input())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, input().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
      
  def inOrder(self):
        current_id = 0
        stack = []
        while True:
            if current_id != -1:
                stack.append(current_id)
                current_id = self.left[current_id]
            elif stack:
                current_id = stack.pop()
                yield self.key[current_id]
                current_id = self.right[current_id]
            else:
                break

  def IsBinarySearchTree(self):
    flag = True 
    if self.n == 0:
        return flag
    start = 0
    flag2 = False
    for x in tree.inOrder():
        if not flag2:
            start = x
            flag2 = True
        else:
            if start < x:
                start  = x
            else:
                flag = False
                break
    return flag
if __name__ == "__main__":
    tree = TreeOrders()
    tree.read()
    if tree.IsBinarySearchTree():
        print("CORRECT")
    else:
        print("INCORRECT")
