

# Day 2 puzzle: https://adventofcode.com/2020/day/2
# In broad terms, count the passwords validated by the policy in place when created.


from puzzles import Puzzle
from supporting import trimmed


class PasswordRequirement:
  def meets(self, password):
    raise NotImplementedError("PasswordRequirement::meets() not implemented!")


# class PasswordPolicy:
#   def __init__(self, requirements):
#     if requirements is None or len(requirements) == 0:
#       raise ValueError("At least one PasswordRequirement is required.")

#     self.requirements = requirements

#   def meets(self, password):
#     valid = True

#     for requirement in self.requirements:
#       valid = requirement.meets(password)
#       if not valid:
#         break

#     return valid


class MinMaxLetter(PasswordRequirement):
  def __init__(self, min, max, letter):
    self.minimum = min
    self.maximum = max
    self.letter = letter

  def meets(self, password):
    return self.minimum <= sum([1 if character == self.letter else 0 for character in password]) <= self.maximum

  def __str__(self):
    return f"[{self.minimum}, {self.maximum}] of the letter '{self.letter}'"

  @staticmethod
  def parse(requirementText):
    range, letter = requirementText.split(" ")
    minimum, maximum = range.split("-")
    return MinMaxLetter(int(minimum), int(maximum), letter)


class ExactlyOnePositioned(PasswordRequirement):
  def __init__(self, left, right, letter):
    # Since there is positioning, we must consider that possibility that
    # the left and right positions could be out of bounds... and... the
    # corporate policy is human-indexed, by that, index(1) is the first
    # character of the policy. If this was Visual Basic... but it's not,
    # so we need to adjust.
    self.left = left - 1
    self.right = right - 1
    self.letter = letter

  def meets(self, password):
    met = self.left < self.right < len(password)

    if met:
      # print(f"Password: {password}; left: {password[self.left]}")
      # Now, test the exactly one (basically, an exclusive or, that must
      # return a positive result) character requirement.

      # To replicate easily, we can use a count of the matches. Here, we
      # only want one match, but we could get up to 2 (left, right).
      matches = 1 if password[self.left] == self.letter else 0
      matches += 1 if password[self.right] == self.letter else 0

      # And apply the exactly one match requirement.
      met = matches == 1

    return met

  def __str__(self):
    return f"[{self.minimum}, {self.maximum}] of the letter '{self.letter}'"

  @staticmethod
  def parse(requirementText):
    positions, letter = requirementText.split(" ")
    left, right = positions.split("-")
    return ExactlyOnePositioned(int(left), int(right), letter)


class ZeroTwo(Puzzle):
  def __init__(self):
    Puzzle.__init__(self, "02")
    #self.passwordPolicy = None # Eh... looks like P2 didn't introduce multiple requirements. Won't need this!
    self.data = None

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

  # def validatePasswords(self):
  #   if self.passwordPolicy is None:
  #     raise ValueError("ZeroTwo::validatePasswords(): A password policy is not defined!")

  #   validPasswords = 0

  #   return validPasswords

  def one(self):
    # The first part of the puzzle examines passwords that should meet a policy requiring
    # that the password should contain at least a minimum and no more than a maximum count
    # of the specified letter.
    count = 0

    if self.data: # TODO: Might want to invert this into raising an exception?
      for policyPasswordLine in self.data:
        policy, password = [str.strip(_) for _ in policyPasswordLine.split(":")] # Kinda assumes there will only be two fields...
        count += 1 if MinMaxLetter.parse(policy).meets(password) else 0

    return count

  def two(self):
    # The second part of the puzzle examines the characters at the specified positions,
    # where exactly only one of those positions can be the character required.
    count = 0

    if self.data: # TODO: Might want to invert this into raising an exception?
      for policyPasswordLine in self.data:
        policy, password = [str.strip(_) for _ in policyPasswordLine.split(":")] # Kinda assumes there will only be two fields...
        count += 1 if ExactlyOnePositioned.parse(policy).meets(password) else 0

    return count

