

from os import path, sep
from supporting import linearDataFile


class Puzzle:
  def __init__(self, day):
    self.day = f"{day:02d}" if isinstance(day, int) else day
    self.data = None # I don't know if this is useful. TODO: Investigate if it can be removed.

  def __puzzle__(self):
    return __file__

  def __puzzleData__(self, name):
    # By default, assume the data is linear, and trim any leading or trailing whitespace.
    return linearDataFile(f"{path.dirname(self.__puzzle__())}{sep}{name}")

  def exampleData(self):
    return self.__puzzleData__("example.txt")

  def generatedData(self):
    return self.__puzzleData__("generated.txt")

  def use(self, data):
    self.data = data

  def one(self):
    raise NotImplementedError("Part 1 of the puzzle is not implemented. No star for you!")

  def two(self):
    raise NotImplementedError("Part 2 of the puzzle is not implemented. No star for you!")

