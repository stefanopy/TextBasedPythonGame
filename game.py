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
        self.location = 'start'

myPlayer = player()

#### Title Screen ####

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() #placeholder until written        
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
    os.system('clear')
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


def start_game():