

from os import sep
from json import loads


# This file is used to load in the results of previous solutions, for the
# purpose of ensuring any changes to the solutions do not deviate from their
# prior results. The actual data is stored in results.json.


KEY_EXAMPLE = "example"
KEY_GENERATED = "generated"


with open("results.json", 'r') as source:
  data = loads(source.read())


def _keys(day, part):
  return (f"D{int(day):02d}", f"P{int(part)}")


def example(day, part):
  d, p = _keys(day, part)
  return data[d][p][KEY_EXAMPLE]


def generated(day, part):
  d, p = _keys(day, part)
  return data[d][p][KEY_GENERATED]

