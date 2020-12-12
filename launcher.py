
from supporting import linearDataFile, asIntegers, trimmed
from zero.one import ZeroOne
from zero.two import ZeroTwo

if __name__ == "__main__":
  puzzle = ZeroOne(2020)

  # Test with the example data in the puzzle's description.
  puzzle.use(asIntegers(linearDataFile("zero/one/example.txt")))

  print(f"D{puzzle.day}P1 (example): {puzzle.one()}")
  print(f"D{puzzle.day}P2 (example): {puzzle.two()}")

  # Then solve the puzzle with the AoC-generated data.
  puzzle.use(asIntegers(linearDataFile("zero/one/generated.txt")))

  print(f"D{puzzle.day}P1 (generated): {puzzle.one()}")
  print(f"D{puzzle.day}P2 (generated): {puzzle.two()}")

  puzzle = ZeroTwo()

  # Test with the example data in the puzzle's description.
  puzzle.use(trimmed(linearDataFile("zero/two/example.txt")))

  print(f"D{puzzle.day}P1 (example): {puzzle.one()}")
  print(f"D{puzzle.day}P2 (example): {puzzle.two()}")

  # Then solve the puzzle with the AoC-generated data.
  puzzle.use(trimmed(linearDataFile("zero/two/generated.txt")))

  print(f"D{puzzle.day}P1 (generated): {puzzle.one()}")
  print(f"D{puzzle.day}P2 (generated): {puzzle.two()}")

