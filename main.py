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

def get_last_period_date():
    """
    Prompt user to enter the last menstrual period date and parse the input for validation.

    Returns:
        datetime.date: The parsed date object representing the last menstrual period date.

    """
    while True:
        user_input_date = input('Enter the date of your last menstrual period (DD/MM/YYYY). ')
        print_separator_line()
        try:
            last_period_date = datetime.strptime(user_input_date, '%d/%m/%Y').date()
            return last_period_date
        except ValueError:
            print('Error: You entered an invalid format. Please enter the date in DD/MM/YYYY.')

def print_separator_line(length=100):
    """
    Print hyphens in a single line as a separator.

    Args:
        length (int, optional): The number of hyphens in a separator line (default: 50)
    """
    print('-' * length)

# def print_newline():
#     """
#     Print newline to create vertical spacing to improve visual appearance in console output.

#     Args:
#         None

#     Returns:
#         None
#     """
#     print('\n')

def main():
    """
    Main function to get user input, calculate and display the information about pregnancy such as
    gestational age in weeks, trimester, estimated due date (EDD) and countdown until EDD.
    """
    print('\nWelcome to Pregnancy Tracker App!\n')
    print_separator_line()

    # # Prompt the user to enter the month, day and year of her last menstrual period
    # last_period_month = int(input('Enter the month of last period: '))
    # last_period_day = int(input('Enter the day of last period: '))
    # last_period_year = int(input('Enter the year of last period: '))
    # last_period_date = datetime(last_period_year, last_period_month, last_period_day).date()

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
    print(f'You are {gestational_age} weeks pregnant.')
    print(f'Trimester: {trimester}')
    print(f"Estimated Due Date: {due_date.strftime('%d/%m/%Y')}")
    print(f'Due Date: {weeks_remaining} week(s) and {days_remaining} day(s)')

if __name__ == "__main__":
    main()
