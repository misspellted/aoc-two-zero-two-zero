# A skeleton file for starting a new day.
# =======================================


# Day 2 puzzle: https://adventofcode.com/2020/day/22
# Playing cards, with crabs! Woo!


from collections import OrderedDict
from functools import reduce
from puzzles import Puzzle
from supporting import trimmed


class Player:
  MARKER = "Player"

  def __init__(self, number):
    self.number = number
    self.deck = list()

  def canPlay(self):
    return 0 < len(self.deck)

  def play(self):
    return self.deck.pop(0)

  def score(self):
    tally = 0

    for index in range(len(self.deck)):
      tally += self.deck[index] * (len(self.deck) - index)

    return tally

  def __str__(self):
    # Generate the Player's deck of cards.
    return f"Player {str(self.number)}\'s deck: {str.join(', ', [str(card) for card in self.deck])}"


def roundWinner(current, candidate):
  # These are player hands, a dictionary entry of player number to their round hand.
  result = current

  # The winner is the player with the high card.

  # print(f"Current winner: {current[0]} at {current[1]}")
  # print(f"Candidate: {candidate[0]} at {candidate[1]}")

  # Check to see if the candidate unseats the incumbent.
  if result[1] < candidate[1]:
    result = candidate

  return result


class Game:
  def __init__(self):
    self.players = OrderedDict()

  def addPlayer(self, player):
    self.players[player.number] = player

  def round(self, number, debug=False):
    # Drop a note indicating which round is being played.
    if debug:
      print(f"-- Round {number} --")
    plays = dict()

    # Display the current player decks.
    if debug:
      for player in self.players.values():
        print(player)

    # Get each player's card play.
    for player in self.players.keys():
      play = self.players[player].play()
      if debug:
        print(f"Player {str(player)} plays: {str(play)}")
      plays[player] = play

    # Gotta have a winner!
    winner = reduce(lambda current, candidate: roundWinner(current, candidate), plays.items())

    # Announce the winner.
    if debug:
      print(f"Player {winner[0]} wins the round!")

    # Collect the the cards to hand to the winner, according to the rules of the game.
    result = [winner[0], winner[1]]
    plays.pop(winner[0])

    # There's only 2 players, at least in the example data, so not sure how this would
    # translate into three or more players, but we'll deal with that... if we have to.
    for player in self.players.keys():
      # We've already handled the winner's case.
      if player != winner[0]:
        result.append(plays[player])
  
    return result

  def play(self, debug=False):
    roundNumber = 0
    while True:
      roundNumber += 1
      roundResult = self.round(roundNumber, debug)

      # Hand the winnings over to the winning player.
      self.players[roundResult[0]].deck.extend(roundResult[1:])

      seatedPlayers = 0

      # Check to see if more rounds are required to play.
      for player in self.players.values():
        if debug:
          print(player)
          print(f"Player {str(player.number)} can still play? {player.canPlay()}")
        seatedPlayers += 1 if player.canPlay() else 0

      # Need at least 2 players to play the game.
      if debug:
        print(f"Seated players: {seatedPlayers}")
      if seatedPlayers < 2:
        break

    # Return the winning player of the game.
    winner = None

    for player in self.players.keys():
      if self.players[player].canPlay(): # They have all the cards!
        winner = self.players[player]
        break

    return winner


class TwoTwo(Puzzle):
  def __init__(self):
    Puzzle.__init__(self, 22)

  def __puzzle__(self):
    return __file__ # This feels... evil! And I like it!

  def use(self, data):
    # Confirm able to import data.
    # for line in data:
    #   print(line)

    # The incoming data, by default, is 'linear', or literally as the lines from the file.
    # May include line-ending whitespace characters... so, we're gonna trim any trailing,
    # or leading whitespace characters.
    # self.data = trimmed(data)
    # We're going to avoid saving the raw input data from now on, if possible.

    # Alright, now to build the Player instances.
    # Meh, just upgrade to the game instance.
    self.game = Game()

    player = None
    for line in trimmed(data):
      if line.startswith(Player.MARKER):
        # Get the player number, avoiding the trailing ':' character.
        player = Player(int(line.split(' ')[1].split(':')[0]))
        # Add the player to the game.
        self.game.addPlayer(player)
      elif 0 < len(line):
        if player is None:
          raise ValueError("A player was expected to exist to get a card for their deck!")

        player.deck.append(int(line))

    # print(f"There are {len(self.players)} player(s) in this game:")

  def one(self):
    # The first part of the puzzle is to calculate the winner's score.

    # Test playing a round.
    # print(self.game.round(1))
    # Test playing another round.
    # print(self.game.round(2))

    return self.game.play(False).score()

  def two(self):
    # The second part of the puzzle ...
    return Puzzle.two(self) # Defer to the parent class to raise the error.

