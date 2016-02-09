#Directions:  The idea is to read throught the code and at the bottom write a general description of what this program does.
#Read it all first
#Then go back and inserts comments line by line explaining what each line does
#Also descrbie what each section does
#Put your name in a comment at the bottom.
#You may look thing up on the internet, but you may NOT run the program.


from sys import exit 



def start(): 
                next = raw_input("> ")
                if next == "START" or next == "start":
                                forest()
                else:
                                print "I'm sorry, I don't understand this command"
                                start()

def dead(reason):
                print "You are dead because", reason
                exit(0)

def forest():
                print "You find yourself in a cold dark forest."
                print "There is a light ahead in the clearing."
                print "What do you do - move forward, or run away?"
                next = raw_input("> ")

                if next == "MOVE FORWARD" or next == "move forward" or next == "Move forward":
                                castle()
                elif next == "RUN AWAY" or next == "run away" or next == "Run away":
                                dead("you ran away!")
                else:
                                print "I'm sorry, I don't understand this command"
                                forest() 

def castle():
                print "You are now standing before a mighty castle."
                print "There are two doors before you."
                print "Door #1 is old, rusty and covered with moss."
                print "Door #2 is white, radiant and brighter than the morning sun."
                print "Which door do you take?"
                next = raw_input("> ")

                if next == "1" or next == "one" or next == "#1":
                                gold_room()
                elif next == "2" or next == "two" or next == "#2":
                                dragon_room()
                else:
                                print "I'm sorry, I don't understand that command"
                                castle()

def gold_room():
                print "You are now in a room filled with gold coins."
                print "How many gold coins will you take?"
                print "Be careful - the Gods of the castle do not reward the greedy!"
                next = int(raw_input("> "))

                if next < 100:
                                print "You were not greedy!"
                                print "Congratulations, you won the game!"
                                exit(0)
                elif next > 100:
                                print "A trap door opens and you fall into a pit filled with spikes!"
                                dead("you got greedy!")
                else:
                                gold_room()

def dragon_room():
                print "You find yourself facing a huge dragon!"
                print "You can either fight or flee!"
                print "What do you do?"
                next = raw_input("> ")

                if next == "fight" or next == "Fight" or next == "FIGHT":
                                dead("you tried to fight a mighty dragon with your bare hands!")
                elif next == "flee" or next == "FLEE" or next == "Flee":
                                print "You run back to the safety of the castle!"

                                castle()
                else:
                                dead("you took too long to decide!")

print "Welcome to the 'Take a Chance'!" 
player_name = raw_input("What should we call you? ")

print "Thank you for playing the game, %s" % player_name
print "Please type in START to begin the game!"
start()