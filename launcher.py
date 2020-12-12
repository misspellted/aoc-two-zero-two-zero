
from supporting import linearDataFile, asIntegers, trimmed
from zero.one import ZeroOne
from zero.two import ZeroTwo
from zero.three import ZeroThree

if __name__ == "__main__":
  puzzle = ZeroOne(2020)

  # Test with the example data in the puzzle's description.
  puzzle.use(asIntegers(linearDataFile(f"zero/one/example.txt")))

  print(f"D{puzzle.day}P1 (example): {puzzle.one()}")
  print(f"D{puzzle.day}P2 (example): {puzzle.two()}")

  # Then solve the puzzle with the AoC-generated data.
  puzzle.use(asIntegers(linearDataFile(f"zero/one/generated.txt")))

  print(f"D{puzzle.day}P1 (generated): {puzzle.one()}")
  print(f"D{puzzle.day}P2 (generated): {puzzle.two()}")

  puzzle = ZeroTwo()

  # Test with the example data in the puzzle's description.
  puzzle.use(trimmed(linearDataFile(f"{puzzle.offset()}/example.txt")))

  print(f"D{puzzle.day}P1 (example): {puzzle.one()}")
  print(f"D{puzzle.day}P2 (example): {puzzle.two()}")

  # Then solve the puzzle with the AoC-generated data.
  puzzle.use(trimmed(linearDataFile(f"{puzzle.offset()}/generated.txt")))

  print(f"D{puzzle.day}P1 (generated): {puzzle.one()}")
  print(f"D{puzzle.day}P2 (generated): {puzzle.two()}")

  puzzle = ZeroThree()

  # Test with the example data in the puzzle's description.
  puzzle.use(puzzle.exampleData())

  print(f"D{puzzle.day}P1 (example): {puzzle.one()}")
  print(f"D{puzzle.day}P2 (example): {puzzle.two()}")

  # # Then solve the puzzle with the AoC-generated data.
  puzzle.use(puzzle.generatedData())

  print(f"D{puzzle.day}P1 (generated): {puzzle.one()}")
  print(f"D{puzzle.day}P2 (generated): {puzzle.two()}")

