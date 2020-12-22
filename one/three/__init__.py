

# Day 13 puzzle: https://adventofcode.com/2020/day/13
# In a broad sense, seems like dealing with availability?
# We'll see what part 2 contributes.


from functools import reduce
from puzzles import Puzzle
from supporting import trimmed


def earlier(current, candidate):
  # These are bus 'instances', a dictionary entry of busId to list of departures times.
  # return candidate if len(candidate[1]) < len(current.values()) else current
  # Might work?? Nope. See notes and link in OneThree::one().
  result = current

  # print(f"Current result: {current[0]} at {current[1][-1]}")

  # Part 2 introduces the 'need' to track the buses that are not time-constrained (x).
  if candidate[0] != OneThree.UNCONSTRAINED:
    # print(f"Checking {candidate[0]}'s schedule...")
    # First sorting - find the shorter the schedule.
    if len(candidate[1]) < len(current[1]):
      # print(f"\tSchedule: {current[1]}")
      result = candidate

    # But what if the candidate has the same number of departures? I bet there's an
    # instance in the generated data (or could be?) of this scenario. If not.. would be
    # an easy-ish test case to do?
    elif len(candidate[1]) == len(current[1]):
      # Then we'll want to take the earlier of the last departure times in the schedule.
      if candidate[1][-1] < current[1][-1]:
        result = candidate

  return result


class Bus:
  def __init__(self, id, position):
    self.id = id
    self.interval = int(id)
    self.position = position

  def departuresAround(self, targetDepartureTime):
    departures = list()

    # Get the departure time just 'missed'.
    departures.append(self.interval * (targetDepartureTime // self.interval))

    # If the bus does not depart exactly on at the target departure time, add
    # the next time the bus would be available.
    if departures[0] != targetDepartureTime:
      departures.append(departures[0] + self.interval)

    return departures

  def departsAt(self, targetDepartureTime):
    return targetDepartureTime % self.interval == 0

class Schedule:
  def __init__(self, busIds):
    self.buses = list()
    for busIdIndex in range(len(busIds)):
      busId = busIds[busIdIndex]
      if busId != OneThree.UNCONSTRAINED:
        self.buses.append(Bus(busId, busIdIndex))

  def earliestBusFor(self, targetDepartureTime):
    departures = {bus.id: bus.departuresAround(targetDepartureTime) for bus in self.buses}

    # print(departures)

    # And the earliest departure would be the shortest list of departures..?
    # earliest = reduce(earlier, departures)

    # Can't use the dictionary directly - the dictionary's keys are used in the reduction
    # data.
    # https://stackoverflow.com/questions/26583381/how-to-use-reduce-with-dictionary
    return reduce(lambda current, candidate: earlier(current, candidate), departures.items())

  def earliestStaggeredDepartures(self, staggering):
    # Got tired of this just going. Gave in, and hopped onto Reddit, as linked
    # on AoC's page, clicked on the calendar for day 13, someone linked to an
    # animation, clicked on that, and now I has feel dumb.

    # Animation reference: https://streamable.com/tojflp

    # I would never have thought to do it that way, but now I'm going to try and
    # implement an algorithm like that, without looking at code, just the anim.
    
    # Don't know how long that animation reference link will stay alive... But
    # it appears to show an increasing interval, instead of the static one I've
    # been using (see this function, in commit 0d489ec).

    # I'm not gonna look up code, but try to derive an algorithm based on that
    # animation. Let's see how long this takes... *sigh*. This is another thing
    # about these kinds of things, why I don't like them. They make me feel dumb.

    # The animation looks to start out by 'normalizing' the bus offsets.
    # In it, we can see all buses start out at their 0 multipliers. They are then
    # shifted up, according to their position in the "scheduling queue", which is
    # seend by Bus 13 staying at 0, but Bus 37 shifting up by 7.
    normalized = { bus.id: bus.position for bus in self.buses }

    # print(normalized)

    # I just noticed... I also have a Bus 13 and Bus 37, in the exact same queue
    # positions. Therefore, I should be able to see a 104 as the first match.
    interval = self.buses[0].interval
    currentDepartureTime = interval
    nextBus = 1

    while nextBus < len(self.buses):
      if self.buses[nextBus].departsAt(currentDepartureTime + normalized[self.buses[nextBus].id]):
        # print(f"Bus {self.buses[nextBus].id} departs at {currentDepartureTime} + position offset {self.buses[nextBus].position}!")
        interval *= self.buses[nextBus].interval
        nextBus += 1
      else:
        currentDepartureTime += interval

    # That is all it was. *shakes head*... Well, I definitely feel the dumbs.

    return currentDepartureTime


class OneThree(Puzzle):
  UNCONSTRAINED = 'x'

  def __init__(self):
    Puzzle.__init__(self, 13)

  def __puzzle__(self):
    return __file__ # This feels... evil! And I like it!

  def use(self, data):
    # The incoming data, by default, is 'linear', or literally as the lines from the file.
    # May include line-ending whitespace characters... so, we're gonna trim any trailing,
    # or leading whitespace characters.
    self.data = trimmed(data)

    # Confirm able to import data.
    # for line in self.data:
    #   print(line)

    # Although, it's looking like it's structured differently than just plain linear. The
    # lines mechanism are there... it's just that the two example lines are not processed
    # in the same manner, as they contain different data.

    self.targetDepartureTime = int(self.data[0])

    self.busIds = self.data[1].split(",")
    self.schedule = Schedule(self.busIds)

  def one(self):
    # The first part of the puzzle is to find the first bus that would get us out by our
    # earliest departure time, do some math on that... and return it.
    earliest = self.schedule.earliestBusFor(self.targetDepartureTime)

    # print(earliest)

    # Now that we know the earliest, we need to know the "penalty" - the id of the bus
    # multiplied by the difference in the bus's departure time and the earliest departure
    # time.

    departureBusId, actualDepartureTime = int(earliest[0]), earliest[1][-1]

    return departureBusId * (actualDepartureTime - self.targetDepartureTime)

  def two(self):
    # The second part of the puzzle tries to find the earliest sequential departure time
    # across all time-constrained buses.
    return self.schedule.earliestStaggeredDepartures(1)

