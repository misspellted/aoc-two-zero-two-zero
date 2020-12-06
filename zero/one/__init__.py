
# Day 1 puzzle: https://adventofcode.com/2020/day/1
# In broad terms, find the product of two numbers, where the sum of those numbers is a particular value.

from functools import reduce
from puzzles import Puzzle

def dodge(index, array):
  # Get all the elements, except the one at the specified index.
  dodged = array[:index]
  dodged.extend(array[index + 1:])
  return dodged

class ZOTreeNode:
  def __init__(self):
    self.objective = None
    self.consumed = list()
    self.remaining = list()
    self.children = list()

  def grow(self): # To maybe make this faster, we could introduce a depth variable here... but... not now.
    grew = False

    # Require at least 2 remaining elements to grow the node and also avoid a negative objective.
    if self.objective is not None and 1 < len(self.remaining):
      possibilities = {self.remaining[index] : dodge(index, self.remaining) for index in range(len(self.remaining))}

      for current, remaining in possibilities.items():
        nextObjective = self.objective - current

        # This assumes all the expenses are a positive value, and thus, any subtraction falling below zero can be ignored.
        if 0 <= nextObjective:
          child = ZOTreeNode()
          child.objective = nextObjective
          child.consumed = list(self.consumed)
          child.consumed.append(current)
          child.remaining = remaining

          child.grow()

          self.children.append(child)
    
      grew = True

    return grew

  def __str__(self):
    return f"Objective: {self.objective}; Consumed: {self.consumed}; Remaining: {len(self.remaining)}; Children: {len(self.children)}"

  def stringify(self):
    # Will likely need to debug this data structure...
    strings = list()
    strings.append(str(self))
    for child in self.children:
      strings.extend([f"  +-- {line}" for line in child.stringify()])
    return strings

  def search(self, targetObjective, depth):
    # Assume no matches are found.
    result = None

    # print(f"Searching for {targetObjective}... looking at {self}")

    if self.objective == targetObjective and len(self.consumed) == depth:
      result = self
    else:
      for child in self.children:
        result = child.search(targetObjective, depth)

        # Find the first result.
        if result is not None:
          break

    return result

class ZOTree:
  def __init__(self, objective, available):
    self.root = ZOTreeNode()
    self.root.objective = objective
    self.root.remaining = available

  def grow(self):
    self.root.grow()

  def __str__(self):
    # Will likely need to debug this data structure...
    allStrings = list()
    allStrings.append(f"[root]")
    allStrings.extend(self.root.stringify())
    return str.join("\n", allStrings)

  def search(self, target, depth):
    return self.root.search(target, depth)

class ZeroOne(Puzzle):
  def __init__(self, targetSum):
    Puzzle.__init__(self, "01")
    self.tree = None
    self.targetSum = targetSum

  def use(self, expenses):
    # Ensure the incoming data is numerically an integer in nature.
    self.tree = ZOTree(self.targetSum, [int(expense) for expense in expenses])

    # Grow the tree. Very inefficiently, in terms of storage and processing, of course!
    self.tree.grow()

    # print(self.tree)

  def findExpenses(self, count):
    # Uh... how do I traverse a tree again?... All I remember is "breadth" versus "depth" searching..
    # Yeah... the terms... not how to implement, LOL!

    # Alright, I think I got it? Depth first it is!
    # print(f"Searching the tree for an Objective of 0, at a depth of {count}...")
    match = self.tree.search(0, count)

    expenses = None

    # A match was found!
    if match is not None:
      # print(f"Match: {match}")

      expenses = list(match.consumed)

    return expenses

  def findAndMultiplyExpenses(self, count):
    result = None

    expenses = self.findExpenses(count)

    if expenses is not None:
      # print(expenses)
      result = reduce(lambda product, term: product * term, expenses)

    return result

  def one(self):
    # The first part of the puzzle is to find a pair of expenses that equals 2020.
    # In the data structure implemented, we reversed the direction, so we're looking
    # for an objective of 0, with a depth of 2?
    return self.findAndMultiplyExpenses(2)

  def two(self):
    # The first part of the puzzle is to find a triplet of expenses that equals 2020.
    # In the data structure implemented, we reversed the direction, so we're [still] looking
    # for an objective of 0, but now with a depth of 3.
    return self.findAndMultiplyExpenses(3)
