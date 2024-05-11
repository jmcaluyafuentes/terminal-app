"""
Pregnancy Tracker Application

Term 1, Assignment 3
Web Development Accelerated Program
Coder Academy

Student/Author: John Fuentes
"""

# Import statements
import sys
from textwrap import dedent
from datetime import datetime, date
from colorama import Fore, Style
import emoji
from print_guide import display_guide_on_top, guide_user_response
from pregnancy_calculator import calc_pregnancy_info
from food_safety import check_food_safety
from travel_safety import check_travel_safety
from activities_safety import check_activities_safety
from user_next_action import get_user_next_action
from user_notes import record_personal_notes, display_personal_notes

# Helper functions
def get_last_period_date() -> date:
    """
    Prompt user to enter the last menstrual period date and parse the input for validation.

    Returns:
        date: The parsed date object representing the last menstrual period date.

    """
    # Display the guide for instructions and for quitting the app
    display_guide_on_top() # From print_guide module

    while True:
        # Prompt user to enter the date of her last menstrual period
        user_input = input('\nEnter the date of your last menstrual period (DD/MM/YYYY): ')
        # Check if user want to view the instructions or exits the app
        instructions = guide_user_response(user_input)

        while not instructions:
            try:
                # Convert user input string into datetime.date object in DD/MM/YYYY format
                last_period_date = datetime.strptime(user_input, '%d/%m/%Y').date()
                # Get current date
                current_date = date.today()
                # Check if last_period_date is before the current date
                if last_period_date < current_date:
                    return last_period_date
                else:
                    # Display the guide for instructions and for quitting the app
                    display_guide_on_top() # From print_guide module
                    # Display error message for invalid input date
                    print(Fore.RED + emoji.emojize(dedent('''
                    :cross_mark: ERROR: The last menstrual period date must be before the current date.
                    ''')) + Style.RESET_ALL)
                    instructions = True
            except ValueError:
                # Display the guide for instructions and for quitting the app
                display_guide_on_top() # From print_guide module
                # Handles error gracefully if user entered invalid date format
                print(Fore.RED + emoji.emojize(dedent(f'''
                :cross_mark: ERROR: "{user_input}" is an invalid format.
                Please enter the date in DD/MM/YYYY.'''
                )) + Style.RESET_ALL)
                instructions = True

def get_travel_date() -> date:
    """
    Prompt user to enter the planned travel date for validation.

    Returns:
        date: The parsed date object representing the date of planned travel.
    """

    while True:
        # Prompt the user the date of her planned travel date
        user_input = input('\nEnter the date of your planned travel (DD/MM/YYYY): ')
        # Check if user want to view the instructions or exits the app
        instructions = guide_user_response(user_input)

        while not instructions:
            try:
                # Convert user input string into datetime.date object in DD/MM/YYYY format
                travel_date = datetime.strptime(user_input, '%d/%m/%Y').date()
                current_date = date.today()
                # Check if last_period_date is before the current date
                if travel_date > current_date:
                    return travel_date
                else:
                    # Display the guide for instructions and for quitting the app
                    display_guide_on_top() # From print_guide module
                    # Display error message for invalid input date
                    print(Fore.RED + emoji.emojize(dedent('''
                    :cross_mark: ERROR: The travel date must be after the current date.
                    ''')) + Style.RESET_ALL)
                    instructions = True
            except ValueError:
                # Display the guide for instructions and for quitting the app
                display_guide_on_top() # From print_guide module
                # Handles error gracefully if user entered invalid date format
                print(Fore.RED + emoji.emojize(dedent(f'''
                :cross_mark: ERROR: "{user_input}" is an invalid format. 
                Please enter the date in DD/MM/YYYY.\n
                ''')) + Style.RESET_ALL)
                instructions = True

# Main functions
def pregnancy_information() -> None:
    """
    Calculate and display the information about pregnancy such as gestational age 
    in weeks, trimester, estimated due date (EDD) and countdown until EDD.
    """
    while True:
        # Prompt the user to enter the date of her last menstrual period
        last_period_date = get_last_period_date()

        # Calculate gestational age in weeks
        gestational_age, trimester, due_date, weeks_remaining, days_remaining = calc_pregnancy_info(last_period_date)

        # Display the guide for instructions and for quitting the app
        display_guide_on_top() # From print_guide module

        # Display relevant information about the pregnancy
        print(Fore.YELLOW + emoji.emojize(dedent(f'''
            Pregnancy Information:\n
            You are {gestational_age} weeks pregnant :baby: \n
            Trimester: {trimester}
            Estimated Due Date: {due_date.strftime('%d/%m/%Y')}
            Due Date Countdown: {weeks_remaining} week(s) and {days_remaining} days.
            ''') + Style.RESET_ALL))

        # Prompt user what she wants to do next
        if not get_user_next_action(): # From user_next_action module

            # Display the guide for instructions and for quitting the app
            display_guide_on_top() # From print_guide module
            break # Return to main menu based on user choice

def food_safety() -> None:
    """
    Prompt the user what food she wants to know on the safety information
    """

    food_safety_loop = True
    while food_safety_loop:
        # Display the guide for instructions and for quitting the app
        display_guide_on_top() # From print_guide module

        # Prompt the user what food she wants to know for the safety information
        user_input = input('Enter a food item: ').lower()

        # Check if user want to view the instructions or exits the app
        instructions = guide_user_response(user_input)

        while not instructions:

            # Calls the function check_food_safety in food_safety module
            food_safety_info, food_precaution, food_handling = check_food_safety(user_input)

            # Display only if the food entered by the user has available safety information
            if food_safety_info:
                print(Fore.YELLOW + f'\nFood: {user_input.capitalize()}\n' + Style.RESET_ALL)
                print(Fore.YELLOW + f'Food Safety Information: {food_safety_info}' + Style.RESET_ALL)

                # Display only if the value in food_precaution is not an empty string
                if food_precaution:
                    print(Fore.YELLOW + f'Precaution: {food_precaution}\n' + Style.RESET_ALL)

                # Display only if the value in food_handling is not an empty string
                if food_handling:
                    print(Fore.YELLOW + f'Food Handling: {food_handling}\n' + Style.RESET_ALL)

            # Inform the user that the food she entered has no available safety information.
            else:
                # Inform user that the food she entered has no available safety information
                print(Fore.RED + f'Sorry, the safety information of "{user_input}" is not available.\n' + Style.RESET_ALL)

            # Prompt the user what she wants to do next
            if not get_user_next_action(): # From user next action module

                # Display the guide for instructions and for quitting the app
                display_guide_on_top() # From print_guide module
                food_safety_loop = False
                break # Return to Safety Information Menu

            instructions = True

def travel_safety(travel_date: date, last_period_date: date) -> None:
    """
    Display the travel information based on the gestational age during the planned travel date.

    Args:
        travel_date (date): The planned travel date.
        last_period_date (date): The date of last menstrual period.
    """
    while True:
        # Obtain the travel information from travel_safety module
        travel_infos = check_travel_safety(travel_date, last_period_date)

        # Display travel safety information with indices from the list
        for index, travel_info in enumerate(travel_infos, 1):
            # Display only if travel info is not an empty string
            if travel_info:
                print(Fore.YELLOW + f'{index}. {travel_info}' + Style.RESET_ALL)

        # Prompt the user what she wants to do next
        if not get_user_next_action(): # From user_next_action function

            # Display the guide for instructions and for quitting the app
            display_guide_on_top() # From print_guide module

            break # Return to main menu based on user choice

        # Display the guide for instructions and for quitting the app
        display_guide_on_top() # From print_guide module

def safety_info() -> None:
    """
    Prompt user to select from the three topics related to safety in pregnancy.
    """
    # Display the guide for instructions and for quitting the app
    display_guide_on_top() # From print_guide module

    while True:
        # Give the user options for the topics related to safety
        print(dedent('''
        Select a topic:\n
        1. Food Safety
        2. Travel Safety
        3. Activities Safety
        '''))

        # Prompt the user her choice
        user_choice = input('Enter your choice (1, 2 or 3) or type "MAIN" to return to main menu: ')

        # Check if user want to view the instructions or exits the app
        instructions = guide_user_response(user_choice)

        while not instructions:
            # Check what the user entered
            if user_choice == '1':
                # Display the food safety information based on user input
                food_safety()
            elif user_choice == '2':
                # Prompt user the date of her last menstrual period
                last_period_date = get_last_period_date()
                # Prompt user the date of her planned travel
                travel_date = get_travel_date()
                # Display the relevant travel safety information
                travel_safety(travel_date, last_period_date)
            elif user_choice == '3':
                # Display the relevant activities safety information
                check_activities_safety() # From activities_safety module
            elif user_choice.lower() == 'main':
                # Go back to main menu
                return None
            else:
                # Display the guide for instructions and for quitting the app
                display_guide_on_top() # From print_guide module

                # Inform the user that she entered an invalid choice
                print(Fore.RED + emoji.emojize(dedent(f'''
                :cross_mark: ERROR: "{user_choice}" is an invalid choice.
                Please enter 1 for Food Safety, 2 for Travel Safety or 3 for Activities Safety.
                Or type "MAIN" to return to main menu.
                ''')) + Style.RESET_ALL)
            instructions = True

def note_taking() -> None:
    """
    This function allows the user to record her personal notes with date and time stamps.
    """
    # Display the guide for instructions and for quitting the app
    display_guide_on_top() # From print_guide module

    note = True
    while note:
        print(dedent('''
            Select an action:\n
            1. Write and record a note
            2. Read the recorded note
            3. Go back to Main Menu
            '''))

        # Prompt the user her choice
        user_choice = input('Enter your choice (1, 2 or 3): ')

        # Check if user want to view the instructions or exits the app
        instructions = guide_user_response(user_choice)

        while not instructions:
            # Check what the user selected
            if user_choice == '1':
                # Get user input and record her notes
                record_personal_notes() # From user_notes module
            elif user_choice == '2':
                # Display user recorded notes
                display_personal_notes() # From user_notes module
            elif user_choice == '3':
                # Display the guide for instructions and for quitting the app
                display_guide_on_top() # From print_guide module
                # Go back to main menu
                note = False
                break
            else:
                # Display the guide for instructions and for quitting the app
                display_guide_on_top() # From print_guide module

                print(Fore.RED + emoji.emojize(dedent(f'''
                    :cross_mark: ERROR: "{user_choice}" is an invalid choice.
                    Please enter 1 to write a note or 2 to read a note.
                    ''')) + Style.RESET_ALL)
            instructions = True

# Execution entry point
def main() -> None:
    """
    Main function that allows the user to select from the features of pregnancy tracker app.
    """
    try:
        # Display the title and guide for the instructions and for quitting the app
        display_guide_on_top() # From print_guide module

        while True:
            # Give user options based on the features of this app
            print(dedent('''
            Select from the following features.\n
            1. Pregnancy Information
            2. Safety Information
            3. Take Down Notes
            '''))

            # Prompt the user of her choice
            user_choice = input('Enter your choice (1, 2 or 3): ')

            # Check if user want to view the instructions or exits the app
            instructions = guide_user_response(user_choice)

            while not instructions:
                # Check what option the user selected
                if user_choice == '1':
                    # Display pregnancy information based on user input
                    pregnancy_information()
                    display_guide_on_top() # From print_guide module
                elif user_choice == '2':
                    # Display safety information based on user input
                    safety_info()
                    display_guide_on_top() # From print_guide module
                elif user_choice == '3':
                    # Record user's personal notes
                    note_taking()
                    display_guide_on_top() # From print_guide module
                else:
                    # Display the guide for instructions and for quitting the app
                    display_guide_on_top() # From print_guide module

                    # Inform the user if she entered invalid choice
                    print(Fore.RED + emoji.emojize(f':cross_mark: ERROR: "{user_choice}" is an invalid choice. Please enter 1, 2 or 3.') + Style.RESET_ALL)
                instructions = True
    # Exit the app if there are keyboard interrupt done by the user such 'Ctrl + C'
    except KeyboardInterrupt:
        print('\n' * 200)
        print(Fore.RED + emoji.emojize('\n:cross_mark: ERROR: Keyboard interrupt received.\n') + Style.RESET_ALL)
        print(Fore.GREEN + 'Thank you for using the Pregnancy Tracker app. Goodbye!\n' + Style.RESET_ALL)
        sys.exit(1)

# Execute main function when the script is run
if __name__ == "__main__":
    main()
