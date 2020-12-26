

from results import example, generated
from two.two import TwoTwo


# Import the unit tests to be run every time the current day's puzzles are run.
from unittest import main
from tests import *


if __name__ == "__main__":
  puzzle = TwoTwo()

  # Test with the example data in the puzzle's description.
  puzzle.use(puzzle.exampleData())

  print(f"D{puzzle.day}P1E: expected {example(puzzle.day, 1)}, actually {puzzle.one()}")
  # print(f"D{puzzle.day}P2E: expected {example(puzzle.day, 2)}, actually {puzzle.two()}")

  # Then solve the puzzle with the AoC-generated data.
  puzzle.use(puzzle.generatedData())

  print(f"D{puzzle.day}P1G: expected {generated(puzzle.day, 1)}, actually {puzzle.one()}")
  # print(f"D{puzzle.day}P2G: expected {generated(puzzle.day, 2)}, actually {puzzle.two()}")

  # Run the unit tests to ensure any changes to puzzle solutions don't break.
  main()

