# Python text RPG
# a game from Stefano

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

#### Player Setup ####

class player: 
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False
        self.job = ''
        

myPlayer = player()

#### Title Screen ####

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game() #placeholder until written        
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command: choose between play, help or quit")
        option = input("> ")
        if option.lower() == ("play"):
            start_game() #placeholder until written        
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('cls')
    print('################################')
    print('#   welcome to the text RPG!   #')
    print('################################')
    print('             - Play -           ')
    print('             - Help -           ')
    print('             - Quit -           ')
    print('    Copyright 2019 Stefano.py   ')
    title_screen_selections()

def help_menu():
    print('################################')
    print('#   welcome to the text RPG!   #')
    print('################################')
    print('- Use up, down, left, right to move')
    print('- Type your commands to do them  -')
    print('- Use look to inspect something -           ')
    print('    Good Luck and have fun   ')
    title_screen_selections()

#### Map ####
"""
a1 a2..... # PLAYER STARTS AT b2
-----------------
| a1  | a2  | a3  | a4  |
-----------------
|  b1 |x| b3  | b4  | 
-----------------
| c1  | c2  | c3  | c4  |
-----------------
|  d1 | d2  | d3  | d4  |   
-----------------
"""

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {
'a1': False, 'a2': False, 'a3': False, 'a4': False,
'b1': False, 'b2': False, 'b3': False, 'b4': False,
'c1': False, 'c2': False, 'c3': False, 'c4': False,
'd1': False, 'd2': False, 'd3': False, 'd4': False,
}

zonemap = {
    'a1':{
        ZONENAME: "Town Market",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : '',
        DOWN : 'b1',
        LEFT : '',
        RIGHT : 'a2',
    },
    'a2':{
        ZONENAME: "Town Entrance",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : '',
        DOWN : 'b2',
        LEFT : 'a1',
        RIGHT : 'a3',
    },
    'a3':{
        ZONENAME: "Town Square",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : '',
        DOWN : 'b3',
        LEFT : 'a2',
        RIGHT : 'a4',
    },
    'a4':{
        ZONENAME: "Town Hall",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : '',
        DOWN : 'b4',
        LEFT : 'a3',
        RIGHT : '',
    },
    'b1':{
        ZONENAME: "Cemetery",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'a1',
        DOWN : 'c1',
        LEFT : '',
        RIGHT : 'b2',
    },
    'b2':{
        ZONENAME: 'Home',
        DESCRIPTION : 'This is your home!',
        EXAMINATION : 'Your home looks the same, nothing has changed.',
        SOLVED : False,
        UP : 'a2',
        DOWN : 'c2',
        LEFT : 'b1',
        RIGHT : 'b3',
    },
    'b3':{
        ZONENAME: "",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : ['up', 'north'],
        DOWN : ['down', 'south'],
        LEFT : ['left', 'west'],
        RIGHT : ['right', 'east'],
    },  
    'b4':{
        ZONENAME: "",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : ['up', 'north'],
        DOWN : ['down', 'south'],
        LEFT : ['left', 'west'],
        RIGHT : ['right', 'east'],
    },
    'c1':{
        ZONENAME: "",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : ['up', 'north'],
        DOWN : ['down', 'south'],
        LEFT : ['left', 'west'],
        RIGHT : ['right', 'east'],
    },
    'c2':{
        ZONENAME: "",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : ['up', 'north'],
        DOWN : ['down', 'south'],
        LEFT : ['left', 'west'],
        RIGHT : ['right', 'east'],
    },
    'c3':{
        ZONENAME: "",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : ['up', 'north'],
        DOWN : ['down', 'south'],
        LEFT : ['left', 'west'],
        RIGHT : ['right', 'east'],
    },
    'c4':{
        ZONENAME: "",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : ['up', 'north'],
        DOWN : ['down', 'south'],
        LEFT : ['left', 'west'],
        RIGHT : ['right', 'east'],
    },
    'd1':{
        ZONENAME: "",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : ['up', 'north'],
        DOWN : ['down', 'south'],
        LEFT : ['left', 'west'],
        RIGHT : ['right', 'east'],
    },
    'd2':{
        ZONENAME: "",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : ['up', 'north'],
        DOWN : ['down', 'south'],
        LEFT : ['left', 'west'],
        RIGHT : ['right', 'east'],
    },
    'd3':{
        ZONENAME: "",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : ['up', 'north'],
        DOWN : ['down', 'south'],
        LEFT : ['left', 'west'],
        RIGHT : ['right', 'east'],
    },
    'd4':{
        ZONENAME: "",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : ['up', 'north'],
        DOWN : ['down', 'south'],
        LEFT : ['left', 'west'],
        RIGHT : ['right', 'east'],
    },
}

#### Game Functionality ####

def start_game():
    return


def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
         # here handle if puzzles have been solved, boss defeated, explored everything, etc.






#### Game Interactivity ####

def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))


def prompt():
    print("\n" + "=======================")
    print("what would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk','quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("You can't do that, try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move','go','travel','walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

def player_move(destination):
    ask = "where would you like to move to? \n"
    dest = input(ask)
    if dest in ['up','north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left','west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['east','right']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['south','down']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)



def movement_handler(destination):
    print("\n" + "you have moved to the " + ".")
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("You have already resolved this zone.")
    else:
        print("You can trigger puzzle here") #skeleton code, add something here








def setup_game():
    os.system('cls')

    #Question for Name
    question1 = "hello, what is your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05) 
    player_name = input("> ")
    myPlayer.name = player_name

    #Question for Job
    question2 = "What role do you want to play? \n"
    question2added = "(You can play as a warrior, mage or priest"
    
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01) 
    
    player_job = input("> ")

    valid_jobs = ['warrior', 'mage', 'priest']

    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are now a " + player_job + "!\n")
    while player_job.lower() not in valid_jobs:
            player_job = input("> ")
    if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are now a " + player_job + "!\n")

    #Player Stats

    if myPlayer.job is 'warrior':
        self.hp = 120
        self.mp = 50
    elif myPlayer.job is 'mage':
        self.hp = 50
        self.mp = 120
    elif myPlayer.job is 'priest':
        self.hp = 80
        self.mp = 80

    #Introduce

    question3 = "Welcome, "+ player_name + " The " + player_job + ".\n"
    
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    

    speech1 = "Welcome to this fantasy worlds \n"
    speech2 = "Just make sure to don't get too lost \n"
    speech3 = "Hehehehehe.... \n"
        
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
       
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
        
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)

    os.system('cls')
    print("##########################")
    print("#    Let's start now!    #")
    print("##########################")
    main_game_loop()

title_screen()