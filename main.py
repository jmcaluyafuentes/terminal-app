"""
Pregnancy Tracker Application

Term 1, Assignment 3
Web Development Accelerated Program
Coder Academy

Author: John Fuentes
"""

from datetime import datetime
from pregnancy_calculator import (
    calculate_gestational_age,
    calculate_trimester,
    calculate_due_date,
    calculate_countdown
)
from food_safety import check_food_safety
from travel_safety import check_travel_safety
from activities_safety import check_activities_safety

def pregnancy_information():
    """
    Calculate and display the information about pregnancy such as gestational age 
    in weeks, trimester, estimated due date (EDD) and countdown until EDD.
    """
    while True:

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
        print(f'Due Date: {weeks_remaining} week(s) and {days_remaining} day(s)')

        print_separator_line()

        while True:
            next_choice = input('What would you like to do next?\n\n'
                                '1. Continue\n'
                                '2. Return to main menu\n'
                                '3. Exit the app\n'
                                'Enter your choice (1, 2 or 3): ')
            
            print_separator_line()

            if next_choice == '1':
                break
            elif next_choice == '2':
                return
            elif next_choice == '3':
                return False
            else:
                print('Invalid choice. Please enter 1 or 2.\n')

def get_last_period_date():
    """
    Prompt user to enter the last menstrual period date and parse the input for validation.

    Returns:
        datetime.date: The parsed date object representing the last menstrual period date.

    """
    while True:
        user_input_date = input('\nEnter the date of your last menstrual period (DD/MM/YYYY): ')

        try:
            last_period_date = datetime.strptime(user_input_date, '%d/%m/%Y').date()
            return last_period_date
        except ValueError:
            print_separator_line()
            print('Error: You entered an invalid format. Please enter the date in DD/MM/YYYY.')

def safety_info():
    """
    Prompt user to select from the three topics related to safety in pregnancy.
    """

    while True:

        print('Select a topic:\n')
        print('1. Food Safety')
        print('2. Travel Safety')
        print('3. Activities Safety\n')

        choice = input('Enter your choice (1, 2 or 3): ')

        print_separator_line()

        if choice == '1':
            food = input('Enter a food item: ').lower()
            food_safety_info = check_food_safety(food)
            print(f'\n{food.capitalize()}: {food_safety_info}')
            print_separator_line()
        elif choice == '2':
            check_travel_safety()
        elif choice == '3':
            check_activities_safety()
        else:
            print('Error: Invalid choice. Please enter 1 for Food Safety, 2 for Travel Safety or 3 for Activities Safety\n')

def note_taking():
    pass

def print_separator_line(length=100):
    """
    Print hyphens in a single line as a separator.

    Args:
        length (int, optional): The number of hyphens in a separator line (default: 50)
    """
    print('-' * length)

def main():
    """
    Main function that allows the user to select from the features of pregnancy tracker app.
    """

    print('\nWelcome to Pregnancy Tracker App!\n')
    print('What would you like to know? ')

    main_menu = True

    while main_menu:
        print('Select from the following list.\n')
        print('1. Pregnancy Information')
        print('2. Safety Information')
        print('3. Take Down Notes\n')

        choice = input('Enter your choice (1, 2 or 3): ')
        print_separator_line()

        if choice == '1':
            main_menu = pregnancy_information()
        elif choice == '2':
            safety_info()
        elif choice == '3':
            note_taking()
        else:
            print('Invalid choice. Please enter 1, 2 or 3.\n')

        # while True:
        #     next_choice = input('What would you like to do next?\n'
        #                         '1. Return to the main menu?\n'
        #                         '2. Exit the app\n'
        #                         'Enter your choice (1 or 2): ')

        #     if next_choice == '1':
        #         break
        #     elif next_choice == '2':
        #         main_menu = False
        #         break
        #     else:
        #         print('Invalid choice. Please enter 1 or 2.\n')

if __name__ == "__main__":
    main()
