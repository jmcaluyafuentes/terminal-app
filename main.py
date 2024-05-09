"""
Pregnancy Tracker Application

Term 1, Assignment 3
Web Development Accelerated Program
Coder Academy

Student/Author: John Fuentes
"""

# Import statements
import sys
from datetime import datetime
from print_guide import guide, instructions
from pregnancy_calculator import (
    calculate_gestational_age,
    calculate_trimester,
    calculate_due_date,
    calculate_countdown
)
from food_safety import check_food_safety
from travel_safety import check_travel_safety
from activities_safety import check_activities_safety

# Helper functions
def get_last_period_date() -> datetime.date:
    """
    Prompt user to enter the last menstrual period date and parse the input for validation.

    Returns:
        datetime.date: The parsed date object representing the last menstrual period date.

    """

    while True:
        print('Enter "QUIT" anytime to exit the app.\n')

        # Prompt user to enter the date of her last menstrual period
        user_input_date = input('Enter the date of your last menstrual period (DD/MM/YYYY): ')
        print_separator_line() # Print one line separator of hyphens for aesthetics only

        # Check if user entered "QUIT" case-insensitive
        user_select_exit(user_input_date)

        try:
            # Convert user input string into datetime.date object in DD/MM/YYYY format
            last_period_date = datetime.strptime(user_input_date, '%d/%m/%Y').date()
            return last_period_date
        except ValueError:
            # Handles error gracefully if user entered invalid date format
            print('Error: You entered an invalid format. Please enter the date in DD/MM/YYYY.\n')

def get_travel_date() -> datetime.date:
    """
    Prompt user to enter the planned travel date for validation.

    Returns:
        datetime.date: The parsed date object representing the date of planned travel.
    """

    while True:
        # Prompt the user the date of her planned travel date
        user_input_date = input('Enter the date of your planned travel (DD/MM/YYYY): ')

        try:
            # Convert user input string into datetime.date object in DD/MM/YYYY format
            travel_date = datetime.strptime(user_input_date, '%d/%m/%Y').date()
            return travel_date
        except ValueError:
            # Handles error gracefully if user entered invalid date format
            print('Error: You entered an invalid format. Please enter the date in DD/MM/YYYY.\n')

def print_separator_line(length=110):
    """
    Print hyphens in a single line as a separator.

    Args:
        length (int, optional): The number of hyphens in a separator line (default is 110).
    """

    # Print a separator line of hyphens for aesthetics only
    print('-' * length)

def get_user_next_action() -> bool:
    """
    Prompt the user for the next action whether to continue in current sub menu, return to main menu or exit.

    Returns:
        bool: True if user chooses to continue or False if user chooses to return to main menu.
    """

    while True:
        # Give user an option to quit the app
        print('Enter "QUIT" anytime to exit the app.\n')

        # Prompt the user to get her response
        next_choice = input('What would you like to do next?\n\n'
                            '1. Continue\n'
                            '2. Return to main menu\n'
                            'Enter your choice (1 or 2): ')

        print_separator_line() # Print separator line of hyphens for aesthetics only

        # Check if user entered 'QUIT' case-insensitive
        user_select_exit(next_choice)

        # Check what choice the user selected
        if next_choice == '1':
            return True
        elif next_choice == '2':
            return False
        else:
            # Inform the user that she entered invalid choice
            print('Invalid choice. Please enter 1, 2 or 3.\n')

def user_select_exit(choice: str) -> None:
    """
    Check if user entered "QUIT" in case-insensitive.

    Args:
        choice (str): What user entered.
    """
    if choice.lower() == 'quit':
        print('\nThank you for using the app. Goodbye!\n')
        sys.exit()

# Main functions
def pregnancy_information() -> None:
    """
    Calculate and display the information about pregnancy such as gestational age 
    in weeks, trimester, estimated due date (EDD) and countdown until EDD.
    """
    while True:

        # Prompt user to enter the date of her last menstrual period
        last_period_date = get_last_period_date()

        # Calculate gestational age in weeks
        gestational_age = calculate_gestational_age(last_period_date)

        # Calculate trimester based on gestational age
        trimester = calculate_trimester(gestational_age)

        # Calculate estimated due date
        due_date = calculate_due_date(last_period_date)

        # Calculate the countdown from current date until due date
        weeks_remaining, days_remaining = calculate_countdown(due_date)

        # Display relevant information about the pregnancy
        print(f'\nYou are {gestational_age} weeks pregnant.\n')
        print(f'Trimester: {trimester}')
        print(f"Estimated Due Date: {due_date.strftime('%d/%m/%Y')}")
        print(f'Due Date Countdown: {weeks_remaining} week(s) and {days_remaining} day(s)')

        print_separator_line() # Print separator line of hyphens for aesthetics only

        # Prompt user what she wants to do next
        if not get_user_next_action():
            break # Return to main menu based on user choice

def safety_info() -> None:
    """
    Prompt user to select from the three topics related to safety in pregnancy.
    """

    while True:

        # Give the user options for the topics related to safety
        print('Select a topic:\n')
        print('1. Food Safety')
        print('2. Travel Safety')
        print('3. Activities Safety\n')

        # Prompt the user her choice
        choice = input('Enter your choice (1, 2 or 3): ')

        print_separator_line() # Print separator line of hyphens for aesthetics only

        # Check what the user entered
        if choice == '1':
            # Prompt the user what food she wants to know for the safety information
            food = input('Enter a food item: ').lower()

            # Checks if user entered 'QUIT' case-insensitive
            user_select_exit(food)

            # Calls the function check_food_safety in food_safety module
            food_safety_info, food_precaution, food_handling = check_food_safety(food)

            # Display only if the food entered by the user has available safety information
            if food_safety_info:
                print(f'\nFood: {food.capitalize()}\n')
                print(f'Food Safety Information: {food_safety_info}')

                # Display only if the value in food_precaution is not an empty string
                if food_precaution:
                    print(f'Precaution: {food_precaution}')

                # Display only if the value in food_handling is not an empty string
                if food_handling:
                    print(f'Food Handling: {food_handling}')

                print_separator_line() # Print separator line of hyphens for aesthetics only

            # Inform the user that the food she entered has no available safety information.
            else:
                print(f'Sorry, the safety information of "{food}" is not available.')
                print_separator_line() # Print separator line of hyphens for aesthetics only

        elif choice == '2':
            # Prompt user the date of her last menstrual period
            last_period_date = get_last_period_date()

            # Prompt user the date of her planned travel
            travel_date = get_travel_date()

            # Obtain the travel information from travel_safety module
            travel_infos = check_travel_safety(travel_date, last_period_date)

            # Display travel safety information with indices
            for index, travel_info in enumerate(travel_infos, 1):
                # Display only if travel info is not an empty string
                if travel_info:
                    print(f'{index}. {travel_info}')

            print_separator_line() # Print separator line as hyphens for aesthetics only

        elif choice == '3':
            check_activities_safety()
        else:
            # Inform the user that she entered an invalid choice
            print('Error: Invalid choice. Please enter 1 for Food Safety, 2 for Travel Safety or 3 for Activities Safety\n')

def note_taking():
    pass

# Execution entry point
def main() -> None:
    """
    Main function that allows the user to select from the features of pregnancy tracker app.
    """

    print('\nWelcome to Pregnancy Tracker App!')

    # Display the guide for instructions and for quitting the app
    guide() # From print_guide module

    while True:
        print_separator_line() # Print separator line of hyphens for aesthetics only

        # Give user options based on the features of this app
        print('Select from the following options.\n')
        print('1. Pregnancy Information')
        print('2. Safety Information')
        print('3. Take Down Notes\n')

        # Prompt the user of her choice
        choice = input('Enter your choice (1, 2 or 3): ')

        print_separator_line() # Print a line of hyphens for aesthetics only

        # Check if user entered 'QUIT' case-insensitive
        user_select_exit(choice)

        # Check what option the user selected
        if choice == '1':
            pregnancy_information()
        elif choice == '2':
            safety_info()
        elif choice == '3':
            note_taking()
        elif choice.lower() == 'instructions':
            instructions()
        else:
            # Inform the user if she entered invalid choice
            print('Invalid choice. Please enter 1, 2 or 3.\n')

# Execute main function when the script is run
if __name__ == "__main__":
    main()
