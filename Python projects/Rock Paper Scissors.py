import random

def play():
	user = input("Select your option: rock, paper, scissors: \n")
	computer = random.choice(["rock", "paper", "scissors"])

	if user == computer:
		return "It is a tie."

	if is_win(user, computer):
		return "You won!"
	return "You lost!"

# r < s, s > p, p > r

def is_win(player, opponent):
	if (player == "rock" and opponent == "scissors") or (player == "scissors" and opponent == "paper") or (player == "paper" and opponent == "rock"):
		return True

while(True):
	print(play())