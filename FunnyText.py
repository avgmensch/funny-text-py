from src import funny
from pyperclip import copy
from sys import argv
from os import system, name

# Clear console
if '-c' in argv:
    system('cls' if name == 'nt' else 'clear')

# Entry note
print("Converted text will be copied to the system clipboard.\n")

# Main loop
while True:
    # Get your input
    text = input('> ')

    # Exit if you type 'e'
    if text == 'e':
        break

    # Make it funny and print it
    text = funny(text, 0)
    print(f'> {text}', end='\n'*2)

    # Copy text to clipboard
    copy(text)
