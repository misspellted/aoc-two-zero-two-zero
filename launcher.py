

from results import example, generated
from zero.three import ZeroThree


# Import the unit tests to be run every time the current day's puzzles are run.
from unittest import main
from tests import *


if __name__ == "__main__":
  # The unit tests for ZeroThree are already included, so this is mainly just a placeholder
  # for ZeroFour (or... a deviation, if I so choose, like OneSeven or TwoFive).
  puzzle = ZeroThree()

  # Test with the example data in the puzzle's description.
  puzzle.use(puzzle.exampleData())

  print(f"D{puzzle.day}P1E: expected {example(puzzle.day, 1)}, actually {puzzle.one()}")
  print(f"D{puzzle.day}P2E: expected {example(puzzle.day, 2)}, actually {puzzle.two()}")

  # Then solve the puzzle with the AoC-generated data.
  puzzle.use(puzzle.generatedData())

  print(f"D{puzzle.day}P1G: expected {generated(puzzle.day, 1)}, actually {puzzle.one()}")
  print(f"D{puzzle.day}P2G: expected {generated(puzzle.day, 2)}, actually {puzzle.two()}")

  # Run the unit tests to ensure any changes to puzzle solutions don't break.
  main()

