import random

# Global Variables
USER_POINTS = 0
COMPUTER_POINTS = 0

def userInput():
	# Takes user input of rock, paper, or scissors.
	# Raises exception if the user enters something other than
	# R, P, or S.
	choice = input("Choose your weapon (Enter R, P, or S): ")

	if choice == 'R' or choice == 'P' or choice == 'S':
		return choice

	else:
		raise Exception("That's not a valid choice.")

def opponentInput():
	# Returns the computer's choice: either rock, paper, or scissors
	choices = ['R', 'P', 'S']

	randomChoice = choices[random.randint(0, 2)]

	print("Computer chooses " + randomChoice)

	return randomChoice

def whoWon(user, computer):
	# Returns whether or not the user or computer won, or if it was a tie

	if user == 'R' and computer == 'S':
		return 'user'
	elif user == 'R' and computer == 'P':
		return 'computer'
	elif user == 'R' and computer == 'R':
		return 'tie'
	elif user == 'P' and computer == 'R':
		return 'user'
	elif user == 'P' and computer == 'P':
		return 'tie'
	elif user == 'P' and computer == 'S':
		return 'computer'
	elif user == 'S' and computer == 'R':
		return 'computer'
	elif user == 'S' and computer == 'P':
		return 'user'
	elif user == 'S' and computer == 'S':
		return 'tie'

def main():
	# main function
	global USER_POINTS, COMPUTER_POINTS
	while True:
		a = userInput()
		b = opponentInput()
		game = whoWon(a, b)

		if game == 'user':
			USER_POINTS += 1
		elif game == 'computer':
			COMPUTER_POINTS += 1

		print("You: " + str(USER_POINTS))
		print("Computer: " + str(COMPUTER_POINTS))


# Call main function
if __name__ == '__main__':
	main()