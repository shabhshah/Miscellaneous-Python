# Rishabh Shah
# 2015
# python game for rock, paper, scissors
# passes bleen test

#import
import time
import random
import sys

#setting variables
computer_options = ["rock", "paper", "scissors"]
computerScore = 0
userScore = 0

#define
def blankLine():
	print " "
def wait(z):
	time.sleep(z)
def playAgainFunc():
	while True:
		playAgain = raw_input("Would you like to play again? (yes/no): ").lower()
		if playAgain == "no":
			blankLine()
			wait(1)
			print "Goodbye"
			wait(1)
			sys.exit()
		if playAgain == "yes":
			blankLine()
			wait(1)
			return
		if playAgain == "n":
			blankLine()
			wait(1)
			print "Goodbye"
			wait(1)
			sys.exit()
		if playAgain == "y":
			blankLine()
			wait(1)
			return
		if playAgain != "no" or playAgain != "n" or playAgain != "yes" or playAgain != "y":
			blankLine()
			wait(1)
			print "You entered something that doesn't exist"
			blankLine()
			wait(1)
			print "Please try again"
			blankLine()
			wait(1)

#title
print "Rock, Paper, Scissors!"
blankLine()
wait(1)

#if c != int():
#	time.sleep(1)
#	print "Does not compute"
#	time.sleep(1)
#	print "Does not compute"
#	time.sleep(1)
#	sys.exit()

while True:
	print "Type your selection when prompted"
	blankLine()
	wait(1)
	print "Press control C to quit"
	blankLine()

	#request input
	wait(1)
	b = raw_input("Shoot!: ")
	blankLine()
	a = b.lower()

	#spell check
	if a != "rock":
		if a != "paper":
			if a != "scissors":
				print "You entered something that doesn't exist"
				blankLine()
				wait(1)
				print "The computer wins, the user loses"
				computerScore += 1
				blankLine()
				wait(1)
				print "Human Score: "+str(userScore)+"   "+"Computer Score: "+str(computerScore)
				blankLine()
				wait(1)
				print "Please try the game again"
				blankLine()
				wait(1)
				continue

	#computer choice
	computer_choice = random.choice(computer_options)

	#display selected choices
	wait(1)
	print "The user selects "+a+"!"
	wait(1)
	blankLine()
	print "The computer selects "+computer_choice+"!"
	blankLine()
	
	#winning the game
	wait(1)
	if computer_choice == "rock" and a == "scissors":
		print "The computer wins, the user loses"
		computerScore += 1
		blankLine()
	if computer_choice == "paper" and a == "rock":
		print "The computer wins, the user loses"
		computerScore += 1
		blankLine()
	if computer_choice == "scissors" and a == "paper":
		print "The computer wins, the user loses"
		computerScore += 1
		blankLine()
	if computer_choice == "paper" and a == "scissors":
		print "The user wins, the copmuter loses"
		userScore += 1
		blankLine()
	if computer_choice == "rock" and a == "paper":
		print "The user wins, the computer loses"
		userScore += 1
		blankLine()
	if computer_choice == "scissors" and a == "rock":
		print "The user wins, the computer loses"
		userScore += 1
		blankLine()
	if computer_choice == a:
		print "The game is a draw"
		blankLine()
	wait(1)
	print "Human Score: "+str(userScore)+"   "+"Computer Score: "+str(computerScore)
	blankLine()
	wait(1)
	playAgainFunc()