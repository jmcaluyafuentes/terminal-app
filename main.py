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

def pregnancy_information():
    """
    Calculate and display the information about pregnancy such as gestational age 
    in weeks, trimester, estimated due date (EDD) and countdown until EDD.
    """
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
    print(f'\nYou are {gestational_age} weeks pregnant.')
    print(f'Trimester: {trimester}')
    print(f"Estimated Due Date: {due_date.strftime('%d/%m/%Y')}")
    print(f'Due Date: {weeks_remaining} week(s) and {days_remaining} day(s)')

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
            print('Error: You entered an invalid format. Please enter the date in DD/MM/YYYY.')

def precautions():
    pass

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
    print('What would you like to know? Select from the following list.')
    print('1. Pregnancy Information')
    print('2. Precautions')
    print('3. Take Down Notes')
    choice = input('Enter your choice (1, 2 or 3): ')

    print_separator_line()

    if choice == '1':
        pregnancy_information()
    elif choice == '2':
        precautions()
    elif choice == '3':
        note_taking()
    else:
        print('Invalid choice.')

if __name__ == "__main__":
    main()
