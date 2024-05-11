"""
This module will print the heading with title in every prompt so that
the user will have an option to view the instructions
or quit the application anywhere in the program.
"""

import sys
from textwrap import dedent
from colorama import Fore, Style

def display_guide_on_top() -> None:
    """
    Display the heading in every prompt.
    """
    # Print new lines to have an illusion that clears the previous outputs
    print('\n' * 200)
    # Print separator line of hyphens
    print('-' * 95) # print separator line of hyphens
    # Print the Pregnancy Tracker app title
    print(Fore.GREEN + Style.BRIGHT + '\nPregnancy Tracker App\n' + Style.RESET_ALL)
    # Print separator line of hyphens
    print('-' * 95) # print separator line of hyphens

    print(Fore.CYAN + dedent('''
    Guide:
    - Type 'INSTRUCTIONS' to display the instructions.
    - Type 'QUIT' to exit the Pregnancy Tracker app.
    - Hit enter after selecting an option or typing a command.
    ''') + Style.RESET_ALL)

def guide_user_response(response: str) -> bool:
    """
    Check if user enters 'INSTRUCTIONS' or 'QUIT' case-insensitive

    Args:
        response (str): User can enter 'INSTRUCTIONS' or 'QUIT' at any given time

    Returns:
        bool: True if the response matches "INSTRUCTIONS" (case-insensitive), otherwise False
    """
    # Check if user wants to view the instructions
    if response.lower() == 'instructions':
        instructions()

        # Display the guide for instructions and for quitting the app
        display_guide_on_top() # From print_guide module

        return True

    # Check if user wants to exit the app
    if response.lower() == 'quit':
        sys.exit()

    return False

def instructions() -> None:
    """
    Display the instructions on how to use the Pregnancy Tracker app.
    """

    while True:
        print('-' * 110) # print separator line of hyphens as aesthetics only

        # Display the instructions
        print(Fore.CYAN + '''
        Instructions

        1. The Pregnancy Tracker App has three main features as follows.
            
            Feature 1: Pregnancy Information
            Description: View details about your pregnancy.
            Details:
                a. Gestational age in weeks.
                b. Trimester range (First, Second or Third)
                c. Estimated Due Date or EDD
                d. Countdown until EDD
            
            Feature 2: Safety Information
            Description: Explore safety guidelines about pregnancy.
            Details:
                a. Food Safety - check safety of specific foods
                b. Travel Safety - learn about safe travel practices
                c. Activities Safety - know the safe activities during pregnancy
            
            Feature 3: Note-taking
            Description: Record personal notes on your pregnancy journey
        
        2. Type the option number to select a feature.
        3. Enter date in format DD/MM/YYYY.
        4. Type 'INSTRUCTIONS' to view these instructions at any given time.
        5. Type 'QUIT' to exit the Pregnancy Tracker app at any given time.
        6. Hit ENTER after you type in the prompt (e.g., option number, INSTRUCTIONS, QUIT)
        ''' + Style.RESET_ALL)

        # User can exit the instructions by entering 'CLOSE'
        user_input = input('Enter "CLOSE" to exit these instructions.\n')
        if user_input.lower() == 'close':
            return None
        if user_input.lower() == 'instructions':
            continue
        elif user_input.lower() == 'quit':
            sys.exit()
        else:
            print(Fore.RED + f'"{user_input}" is an invalid choice.' + Style.RESET_ALL)
