#Directions:  The idea is to read throught the code and at the bottom write a general description of what this program does.
#Read it all first
#Then go back and inserts comments line by line explaining what each line does
#Also descrbie what each section does
#Put your name in a comment at the bottom.
#You may look thing up on the internet, but you may NOT run the program.

#this imports the exit command from the module "sys"
from sys import exit 


#this defines the function start that will be used later
def start():
                                #this sets the variable next to whatever the user inputs
                next = raw_input("> ")

                #this lets the program continue to the next stage if the input is correct
                if next == "START" or next == "start":
                                #this runs the function forest
                                forest()
                
                #this lets the program retry this function if the input is not correct
                else:
                                print "I'm sorry, I don't understand this command"
                                #this runs the start function, so if the user input doesn't work, the program will not crash
                                start()

#this defines the dead function which requires a string in between the parenthesis
def dead(reason):
                                #this prints why the user is dead, using the variable reason, which is set when calling the function
                print "You are dead because", reason
                #this exits the program
                exit(0)

#this defines the forest function which is run from within the start function
def forest():
                print "You find yourself in a cold dark forest."
                print "There is a light ahead in the clearing."
                print "What do you do - move forward, or run away?"
                #this sets the variable next to whatever the user inputs
                next = raw_input("> ")

                #this lets the program continue to the next stage if the input is correct
                if next == "MOVE FORWARD" or next == "move forward" or next == "Move forward":
                                #this runs the function castle
                                castle()

                #this lets the program continue to the next stage if the input is correct
                elif next == "RUN AWAY" or next == "run away" or next == "Run away":
                                #this runs the dead function with the string within the parenthesis
                                dead("you ran away!")
                #this lets the program retry this function if the input is not correct
                else:
                                print "I'm sorry, I don't understand this command"
                                #this runs the forest function, so if the user input doesn't work, the program will not crash
                                forest() 

#this defines the castle function which is run from within the forest function
def castle():
                print "You are now standing before a mighty castle."
                print "There are two doors before you."
                print "Door #1 is old, rusty and covered with moss."
                print "Door #2 is white, radiant and brighter than the morning sun."
                print "Which door do you take?"
                #this sets the variable next to whatever the user inputs
                next = raw_input("> ")

                #this lets the program continue to the next stage if the input is correct
                if next == "1" or next == "one" or next == "#1":
                                #this runs the function gold_room
                                gold_room()
                #this lets the program continue to the next stage if the input is correct                                
                elif next == "2" or next == "two" or next == "#2":
                                #this runs the function dragon_room
                                dragon_room()
                #this lets the program retry this function if the input is not correct              
                else:
                                print "I'm sorry, I don't understand that command"
                                #this runs the castle function, so if the user input doesn't work, the program will not crash
                                castle()

#this defines the gold_room function which is run from within the castle function
def gold_room():
                print "You are now in a room filled with gold coins."
                print "How many gold coins will you take?"
                print "Be careful - the Gods of the castle do not reward the greedy!"
                #this sets the variable next to whatever the user inputs                
                next = int(raw_input("> "))

                #this lets the program continue to the next stage if the input is correct
                if next < 100:
                                print "You were not greedy!"
                                print "Congratulations, you won the game!"
                                #this exits the program
                                exit(0)
                #this lets the program continue to the next stage if the input is correct
                elif next > 100:
                                print "A trap door opens and you fall into a pit filled with spikes!"
                                #this runs the dead function with the string within the parenthesis
                                dead("you got greedy!")
                #this lets the program retry this function if the input is not correct
                else:
                                                #this runs the castle function, so if the user input doesn't work, the program will not crash
                                gold_room()

#this defines the dragon_funciton function which is run from within the castle function
def dragon_room():
                print "You find yourself facing a huge dragon!"
                print "You can either fight or flee!"
                print "What do you do?"
                #this sets the variable next to whatever the user inputs
                next = raw_input("> ")

                #this lets the program continue to the next stage if the input is correct
                if next == "fight" or next == "Fight" or next == "FIGHT":
                                                #this runs the dead function with the string within the parenthesis
                                dead("you tried to fight a mighty dragon with your bare hands!")

                #this lets the program continue to the next stage if the input is correct
                elif next == "flee" or next == "FLEE" or next == "Flee":
                                print "You run back to the safety of the castle!"
                                #this runs the function castle
                                castle()

                #this lets the program continue to the next stage if the input is correct
                else:
                                                #this runs the dead function with the string within the parenthesis
                                dead("you took too long to decide!")

print "Welcome to the 'Take a Chance'!" 
#this sets the variable player_name to what the user inputs
player_name = raw_input("What should we call you? ")

#this prints the statement and the string. The %s tells python to look at the end of the line to figure out what the string really is
print "Thank you for playing the game, %s" % player_name
print "Please type in START to begin the game!"

#this runs the start function, which runs the game
start()

#Rishabh Shah