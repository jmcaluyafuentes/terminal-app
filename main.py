"""
Pregnancy Tracker Application

Term 1, Assignment 3
Web Development Accelerated Program
Coder Academy

Student/Author: John Fuentes
"""

from datetime import datetime
import sys
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
        print(f'Due Date Countdown: {weeks_remaining} week(s) and {days_remaining} day(s)')

        print_separator_line()

        # user_quit = input('Enter a command or type "QUIT" to exit: ')

        # if user_quit.strip().lower() == 'quit':
        #     print('Thank you for using the app. Goodbye!')
        #     sys.exit()

        if not get_user_next_action():
            break # Return to main menu

def get_last_period_date():
    """
    Prompt user to enter the last menstrual period date and parse the input for validation.

    Returns:
        datetime.date: The parsed date object representing the last menstrual period date.

    """
    while True:
        user_input_date = input('Enter the date of your last menstrual period (DD/MM/YYYY): ')

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

            # Calls the function check_food_safety(food) in food_safety module
            available, food_safety_info, food_precaution, food_handling = check_food_safety(food)

            if available:
                print(f'\nFood: {food.capitalize()}\n')
                print(f'Food Safety Information: {food_safety_info}')
                if food_precaution:
                    print(f'Precaution: {food_precaution}')
                if food_handling:
                    print(f'Food Handling: {food_handling}')

                print_separator_line()
            else:
                print(f'Safety information of "{food}" is not available.')
                print_separator_line()

        elif choice == '2':
            check_travel_safety()
        elif choice == '3':
            check_activities_safety()
        else:
            print('Error: Invalid choice. Please enter 1 for Food Safety, 2 for Travel Safety or 3 for Activities Safety\n')

def note_taking():
    pass

def print_separator_line(length=110):
    """
    Print hyphens in a single line as a separator.

    Args:
        length (int, optional): The number of hyphens in a separator line (default: 50)
    """
    print('-' * length)

def get_user_next_action():
    """
    Prompt the user for the next action whether to continue in current sub menu, return to main menu or exit.

    Returns:
        bool: True is user chooses to continue, False if user chooses to return to main menu.
    """
    while True:
        next_choice = input('What would you like to do next?\n\n'
                            '1. Continue\n'
                            '2. Return to main menu\n'
                            '3. Exit the app\n'
                            'Enter your choice (1, 2 or 3): ')

        print_separator_line()

        if next_choice == '1':
            return True
        elif next_choice == '2':
            return False
        elif next_choice == '3':
            print('Thank you for using the app. Goodbye!')
            sys.exit()
        else:
            print('Invalid choice. Please enter 1, 2 or 3.\n')

def main():
    """
    Main function that allows the user to select from the features of pregnancy tracker app.
    """

    print('\nWelcome to Pregnancy Tracker App!\n')

    main_menu = True

    while main_menu:
        print('Select from the following options.\n')
        print('1. Pregnancy Information')
        print('2. Safety Information')
        print('3. Take Down Notes')
        print('4. Exit\n')

        choice = input('Enter your choice (1, 2, 3 or 4): ')
        print_separator_line()

        if choice == '1':
            pregnancy_information()
        elif choice == '2':
            safety_info()
        elif choice == '3':
            note_taking()
        elif choice == '4':
            print('Thank you for using the app. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter 1, 2, 3 or 4.\n')

if __name__ == "__main__":
    main()
