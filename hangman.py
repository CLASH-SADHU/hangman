import random
from words import word_list
def print_design(guesses,word):
	if (guesses == 0):
		print("______\n"
		      "|    |\n"
			  "|\n"
			  "|\n"
			  "|\n"
			  "|\n"
			  "|\n")
	elif (guesses == 1):
		print("______\n"
		      "|    |\n"
			  "|    o\n"
			  "|\n"
			  "|\n"
			  "|\n"
			  "|\n")
	elif (guesses == 2):
		print("______\n"
		      "|    |\n"
			  "|    o\n"
			  "|    |/\n"
			  "|\n"
			  "|\n"
			  "|\n")
	elif (guesses == 3):
		print("______\n"
		      "|    |\n"
			  "|    o\n"
			  "|   \|/\n"
			  "|\n"
			  "|\n"
			  "|\n")
	elif (guesses == 4):
		print("______\n"
		      "|    |\n"
			  "|    o\n"
			  "|   \|/\n"
			  "|    |\n"
			  "|\n"
			  "|\n")
	elif (guesses == 5):
		print("______\n"
		      "|    |\n"
			  "|    o\n"
			  "|   \|/\n"
			  "|    |\n"
			  "|   /\n"
			  "|\n")
	elif (guesses == 6):
		print("______\n"
		      "|    |\n"
			  "|    o\n"
			  "|   \|/\n"
			  "|    |\n"
			  "|   / \ \n"
			  "|\n")
def randomword():
	my_word = random.choice(word_list)
	my_word = my_word.lower()
	return my_word

def resume():
	
			print("Do you want to play again?,if so press y for yes n for no")
			again = input(">")
			if again == 'y':
				hangman()
			else:
				quit()
def hangman():
	mode = input("Enter 1 for 1-player mode or 2 for 2-player mode: ").lower()
	if (mode == "1"):
		word = randomword()
	elif (mode == "2"):
		word = input("Player 1 enter the word to guess for Player 2: ")
		print(chr(27) + "[2J") 
	guesses = 0

	wordlist = list(word) 
	blanks = "_""" *len(word)
	blanks_list = list(blanks)
	new_blank_list = list(blanks)
	guessed_list = []
	print("Let's play hangman!!")
	print("It is a",len(word),"chracter word")
	print("\n"+''.join(blanks_list))
	
	while guesses < 6:
		print("Guess a letter:")
		guess = input(">")
		guess = guess.lower()

		if len(guess) > 1:
			print("Enter one letter at a time")
		elif guess == "":
			print("Enter a letter")
		elif guess in guessed_list:
			print("You have already guessed the letter")
		else:
			guessed_list.append(guess)
			i = 0
			while i<len(word):
				if guess == word[i]:
					new_blank_list[i] = word[i]
				i += 1
			if new_blank_list == blanks_list:
				print("Your letter is not in the word")
				guesses += 1
				print_design(guesses,word)

				if guesses < 6:
					print ("Wrong Guess")
					print(''.join(blanks_list))
				
				if guesses == 6:
					print("You Loose,The correct word is",word)
					resume()
				
			elif new_blank_list != blanks_list:
				print ("Right Guess")
				blanks_list = new_blank_list[:]
				print(''.join(blanks_list)) 
			if wordlist == blanks_list:
				print("You win")
				resume()
				
hangman()