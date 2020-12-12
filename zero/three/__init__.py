

# Day 3 puzzle: https://adventofcode.com/2020/day/3
# In broad terms, count the passwords validated by the policy in place when created.


from functools import reduce
from puzzles import Puzzle
from supporting import trimmed


class ZeroThree(Puzzle):
  TREE = '#'

  def __init__(self):
    Puzzle.__init__(self, "03")

  def __puzzle__(self):
    return __file__ # This feels... evil! And I like it!

  def use(self, data):
    # The incoming data, by default, is 'linear', or literally as the lines from the file.
    # May include line-ending whitespace characters... so, we're gonna trim any trailing,
    # or leading whitespace characters.
    self.data = trimmed(data)

  def traverse(self, right, down):
    x, y = (0, 0)  # We always start at the top-left of the map.

    columns = len(self.data[0])
    trees = 0 # And the top-left is [supposedly] garaunteed to be lacking trees.

    while y < len(self.data): # The length of the data is the number of rows in the map.
      # print(f"map[{x},{y}] = {self.data[y][x]}")
      trees += 1 if self.data[y][x] == ZeroThree.TREE else 0
      # Roll around to the beginning of the map (effectively copying it to the right).
      x = (x + right) % columns
      y += down

    return trees

  def one(self):
    # The first part of the puzzle counts the number of trees encounterd on the map, with
    # a slope of right 3, down 1.
    return self.traverse(3, 1)

  def two(self):
    # The second part of the puzzle counts the number of trees encounterd on the map, over
    # a collection of iterations slope of right and down; each iteration's result is then
    # multiplied to the other counts, to arrive at the final answer.
    iterations = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    # result = reduce(lambda product, term: product * term, expenses)
    # Heh, reduce() comes in handy again! Migh'zzle get some more practice using it.
    return reduce(lambda product, term: product * term, [self.traverse(right, down) for right, down in iterations])

