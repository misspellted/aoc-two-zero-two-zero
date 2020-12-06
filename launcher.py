
from supporting import linearDataFile, asIntegers
from zero.one import ZeroOne

if __name__ == "__main__":
  puzzle = ZeroOne(2020)

  # Test with the example data in the puzzle's description.
  puzzle.use(asIntegers(linearDataFile("zero/one/example.txt")))

  print(f"Day {puzzle.day}, Part 1 - The solution with the example data: {puzzle.one()}")
  print(f"Day {puzzle.day}, Part 2 - The solution with the example data: {puzzle.two()}")

  # Then solve the puzzle with the AoC-generated data.
  puzzle.use(asIntegers(linearDataFile("zero/one/generated.txt")))

  print(f"Day {puzzle.day}, Part 1 - The solution with the generated data: {puzzle.one()}")
  print(f"Day {puzzle.day}, Part 2 - The solution with the generated data: {puzzle.two()}")
