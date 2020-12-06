
class Puzzle:
  def __init__(self, day):
    self.day = day
    self.data = None

  def use(self, data):
    self.data = data

  def one(self):
    raise NotImplementedError("Part 1 of the puzzle is not implemented. No star for you!")

  def two(self):
    raise NotImplementedError("Part 2 of the puzzle is not implemented. No star for you!")
