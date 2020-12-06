
# Provide common capabilities supporting solutions for the puzzle of the day.

def linearDataFile(filePath):
  linearData = None

  with open(filePath) as file:
    linearData = file.readlines()

  return linearData

def asIntegers(linearData):
  return [int(line) for line in linearData]
