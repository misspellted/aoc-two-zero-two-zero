

# Day 12 puzzle: https://adventofcode.com/2020/day/12
# In a broad sense, this is like an inertia measurement system.


from puzzles import Puzzle
from supporting import trimmed


class OneTwo(Puzzle):
  DIRECTIONS = "ENWS"

  def __init__(self):
    Puzzle.__init__(self, "12")
    self.reactions = {
      "F": self.forward,
      "L": self.left,
      "R": self.right,
      "E": self.east,
      "N": self.north,
      "W": self.west,
      "S": self.south
    }
    self.reset()

  def reset(self, waypoint=False):
    self.position = [0, 0]             # The ship starts where it starts.
    self.facing = OneTwo.DIRECTIONS[0] # The ship starts facing east.

    if waypoint:
      # For the second part, a waypoint is introduced. It starts out 10 units
      # east and 1 unit north of the ship's position.
      self.waypoint = [10, 1]

  def __puzzle__(self):
    return __file__ # This feels... evil! And I like it!

  def use(self, data):
    # Confirm able to import data.
    # for line in data:
    #   print(line)

    # The incoming data, by default, is 'linear', or literally as the lines from the file.
    # May include line-ending whitespace characters... so, we're gonna trim any trailing,
    # or leading whitespace characters.
    # Expand the data into a lists of tuples (action, magnitude).
    self.data = [(action[0], int(action[1:]))for action in trimmed(data)]

  def forward(self, magnitude, waypoint=False):
    # For the second part, a waypoint is introduced. If not using a waypoint,
    # then we're in part 1, and we should maintain compatibility.
    if not waypoint:
      # self.facing will be one of ENWS, so we can get the faced direction index
      # via a lookup, and then apply any modifiers accordingly.
      direction = OneTwo.DIRECTIONS.index(self.facing)

      # E or N would be positive (+x or +y).
      # W or S would be negative (-x or -y).
      # Therefore, if 0 <= direction <= 1 -> positive movement relative to origin,
      # and 2 <= direction <= 3 -> negative movement relative to origin.
      delta = magnitude * (1 if 0 <= direction <= 1 else -1)

      # And then, the axis to apply it to is indicated as the modulus of 2:
      # E or W would be 0 or 2 -> 0, N or S would be 1 or 3 -> 1.
      # if direction % 2 == 0:
      #   self.position[0] += delta
      # Actually... we can use that to our advantage (nice! this was not planned!).
      self.position[direction % 2] += delta
    else:
      # In part 2, moving forward is now moving the ship towards the waypoint
      # $magnitude times. The waypoint is relative to the current position of
      # the ship, so it won't change.
      self.position[0] += self.waypoint[0] * magnitude
      self.position[1] += self.waypoint[1] * magnitude


  def shift(self, magnitude):
    # Ensure a positive angle.
    delta = magnitude
    while delta < 0:
      delta += 360

    # So that we can divide by the axial angle differences, after constraining
    # the rotation to just one complete revolution.
    # ASSUMPTION: Only cardinal directions!
    return (delta % 360) // 90

  def left(self, magnitude, waypoint=False):
    # For the second part, a waypoint is introduced. If not using a waypoint,
    # then we're in part 1, and we should maintain compatibility.
    if not waypoint:
      # Rotating left is counter-clockwise rotation, so the direction index shift
      # will be negative, but ensure the new index is positive.
      new = OneTwo.DIRECTIONS.index(self.facing) + self.shift(magnitude)
      new = new % len(OneTwo.DIRECTIONS)
      self.facing = OneTwo.DIRECTIONS[new]
    else:
      # Rotating left is counter-clockwise rotation, but now the rotation is
      # applied to the waypoint, which relative to the position of the ship.

      # After some pen and paper figurating, the first plan I have.. requires
      # looping, to apply the rotation.
      # If W[t=0] = (x, y), then a left(90) would result in W[t=1] = (-y, x).
      # The looping occurs for each 90 degress of rotation to perform.
      remaining = magnitude
      while 0 < remaining:
        wx, wy = self.waypoint
        self.waypoint = [-wy, wx]
        remaining -= 90

  def right(self, magnitude, waypoint=False):
    # For the second part, a waypoint is introduced. If not using a waypoint,
    # then we're in part 1, and we should maintain compatibility.
    if not waypoint:
      # Rotating right is clockwise rotation, so the direction index shift will
      # be positive.
      new = OneTwo.DIRECTIONS.index(self.facing) - self.shift(magnitude)
      new = (new + len(OneTwo.DIRECTIONS)) % len(OneTwo.DIRECTIONS)
      self.facing = OneTwo.DIRECTIONS[new]
    else:
      # Rotating right is clockwise rotation, but now the rotation is applied
      # to the waypoint, which relative to the position of the ship.

      # After some pen and paper figurating, the first plan I have.. requires
      # looping, to apply the rotation.
      # If W[t=0] = (x, y), then a right(90) would result in W[t=1] = (y, -x).
      # The looping occurs for each 90 degress of rotation to perform.
      remaining = magnitude
      while 0 < remaining:
        wx, wy = self.waypoint
        self.waypoint = [wy, -wx]
        remaining -= 90

  def east(self, magnitude, waypoint=False):
    # For the second part, a waypoint is introduced. If not using a waypoint,
    # then we're in part 1, and we should maintain compatibility.
    if not waypoint:
      self.position[0] += magnitude
    else:
      # The waypoint is what is moved.
      self.waypoint[0] += magnitude

  def north(self, magnitude, waypoint=False):
    # For the second part, a waypoint is introduced. If not using a waypoint,
    # then we're in part 1, and we should maintain compatibility.
    if not waypoint:
      self.position[1] += magnitude
    else:
      # The waypoint is what is moved.
      self.waypoint[1] += magnitude

  def west(self, magnitude, waypoint=False):
    # For the second part, a waypoint is introduced. If not using a waypoint,
    # then we're in part 1, and we should maintain compatibility.
    if not waypoint:
      self.position[0] -= magnitude
    else:
      # The waypoint is what is moved.
      self.waypoint[0] -= magnitude

  def south(self, magnitude, waypoint=False):
    # For the second part, a waypoint is introduced. If not using a waypoint,
    # then we're in part 1, and we should maintain compatibility.
    if not waypoint:
      self.position[1] -= magnitude
    else:
      # The waypoint is what is moved.
      self.waypoint[1] -= magnitude

  def traverse(self, waypoint=False):
    self.reset(waypoint)

    for action, magnitude in self.data:
      # print(f"Position before action: {self.position}, facing {self.facing}")
      # if waypoint:
      #   print(f"\tWaypoint after action: {self.waypoint}")
      # print(f"Action: {action} @ {magnitude}")

      # if action == "F":
      #   self.forward(magnitude)
      # That's... gonna be a bit. All the actions have a magnitude, so we can
      # look up the reactionary tracking method and pass in the magnitude!
      self.reactions[action](magnitude, waypoint)

      # print(f"Position after action: {self.position}, facing {self.facing}")
      # if waypoint:
      #   print(f"\tWaypoint after action: {self.waypoint}")


    return sum([abs(_) for _ in self.position])

  def one(self):
    # The first part of the puzzle calculates the ship's 'Manhattan distance',
    # or the sum of the absolute values of it's east/west position and it's
    # north/south position, in relation to it's starting position.
    # print(f"Starting by facing {self.facing}")
    return self.traverse()

  def two(self):
    # The second part of the puzzle introduces a waypoint mechanism, altering a
    # large portion of the reactions. See reaction methods for details.
    return self.traverse(True)

