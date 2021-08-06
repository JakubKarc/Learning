import math
import random

class Player:
	def __init__(self, letter):
		# Letter is X or O
		self.letter = letter

	# We want all players to get their next move given a game
	def get_move(self, game):
		pass

class RandomComputerPlayer(Player):
	def __init__(self, letter):
		super().__init__(letter)

	def get_move(self, game):
		square = random.choice(game.available_moves)
		return square

class HumanPlayer(Player):
	def __init__(self, letter):
		super().__init__(letter)

	def get_move(self, game):
		valid_square = False
