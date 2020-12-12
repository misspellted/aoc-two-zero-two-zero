

from os import path, sep
from supporting import linearDataFile


class Puzzle:
  OFFSETS = {'0': "zero", '1': "one", '2': "two"}

  def __init__(self, day):
    self.day = day
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

  def offset(self):
    # WIP: Get the "offset" into the data directory for the data of the puzzle.
    offsets = [Puzzle.OFFSETS[_] for _ in self.day]
    return f"{str.join(sep, offsets)}"

  def one(self):
    raise NotImplementedError("Part 1 of the puzzle is not implemented. No star for you!")

  def two(self):
    raise NotImplementedError("Part 2 of the puzzle is not implemented. No star for you!")

