# A skeleton file for starting a new day.
# =======================================


# Day k puzzle: https://adventofcode.com/2020/day/k
# [broad-description]


from puzzles import Puzzle
from supporting import trimmed


class DayName(Puzzle):
  def __init__(self):
    Puzzle.__init__(self, "[dayNumber:02d]")

  def __puzzle__(self):
    return __file__ # This feels... evil! And I like it!

  def use(self, data):
    # Confirm able to import data.
    # for line in data:
    #   print(line)

    # The incoming data, by default, is 'linear', or literally as the lines from the file.
    # May include line-ending whitespace characters... so, we're gonna trim any trailing,
    # or leading whitespace characters.
    self.data = trimmed(data)

  def one(self):
    # The first part of the puzzle ...
    return Puzzle.one(self) # Defer to the parent class to raise the error.

  def two(self):
    # The second part of the puzzle ...
    return Puzzle.two(self) # Defer to the parent class to raise the error.

