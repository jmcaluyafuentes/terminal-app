"""
This module is used to check travel safety information in CSV file.
"""

import csv
from textwrap import dedent
from datetime import date
from colorama import Fore, Style
from print_guide import display_guide_on_top, guide_user_response
from pregnancy_calculator import calc_gestational_age

def calc_gestational_age_on_travel(travel_date: date, last_period_date: date) -> int:
    """
    Calculate the number of weeks pregnant on the planned travel date.

    Args:
        travel_date (date): The planned travel date.
        last_period_date (date): The date of last menstrual period.
    
    Returns:
        int: The number of weeks pregnant on the planned travel date.
    """

    # Calculate gestational age in weeks
    gestational_age_in_weeks = calc_gestational_age(last_period_date) # From pregnancy_calculator module

    # Calculate the number of weeks from current date to the travel date
    weeks_until_travel = (travel_date - last_period_date).days // 7

    # Calculate the gestational age (in weeks) on the planned travel date
    weeks_pregnant_on_travel = gestational_age_in_weeks + weeks_until_travel

    return weeks_pregnant_on_travel

def check_travel_safety(travel_date: date, last_period_date: date) -> tuple[str, str, str, str, str]:
    """
    Display the travel information based on the gestational age during the planned travel date.

    Args:
        travel date (date): Planned travel date.
        last_period_date (date): Last day of menstrual period

    Returns:
        tuple[str, str, str, str, str]: Several safety information about travel.
    """

    try:
        # Calculate the gestational age (in weeks) on the planned travel date
        weeks_pregnant_on_travel = calc_gestational_age_on_travel(travel_date, last_period_date)

        # Display to user the gestational age (in weeks) on the planned travel date
        print(Fore.YELLOW + dedent(f'''
        \nGeneral Information:
        You will be {weeks_pregnant_on_travel} weeks pregnant during your planned travel on {travel_date.strftime("%d/%m/%Y")}.
        ''') + Style.RESET_ALL)

        # Check if user is on 2nd semester on planned travel date.
        if 13 <= weeks_pregnant_on_travel <= 26:
            print(Fore.YELLOW + dedent('''
                Remarks:
                You will be in 2nd trimester during your planned travel date.
                2nd semester is the safest to travel, provided you are not experiencing any complications.\n
            ''') + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + 'Please consult with your doctor, especially if your pregnancy is high risk.\n' + Style.RESET_ALL)

        questions_list = dedent('''The following are possible questions related to travel safety.\n
            Question 1: What are the general considerations when planning to travel?
            Question 2: What are the complications that a pregnant woman encounters?
            Question 3: What are the travel immunization warnings for pregnant women?
            Question 4: What are the risks of long-distance travel during pregnancy?
            Question 5: How to avoid deep vein thrombosis (DVT) when traveling?
            Question 6: What are the considerations in air travel?
            Question 7: What are the considerations when traveling by car?
            Question 8: What are the considerations if traveling in hot weather?
            Question 9: How to avoid food poisoning during travel?\n
            ''')

        while True:
            # Give the user the list of questions as a guide
            print(Fore.MAGENTA + questions_list + Style.RESET_ALL)

            # Prompt the user what question she would like an answer about the travel information
            user_choice = input('Please enter the number of your choice: ')

            # Check if user want to view the instructions or exits the app
            instructions = guide_user_response(user_choice)

            if not instructions:
                try:
                    user_selected_int = int(user_choice)
                except ValueError:
                    # Display the guide for instructions and for quitting the app
                    display_guide_on_top() # From print_guide module

                    print(Fore.RED + f'Error: "{user_choice}" is invalid: Please enter from 1 to 9.\n' + Style.RESET_ALL)
                    continue

                if 1 <= user_selected_int <= 9:
                    # Start the zero-based index at the first question item
                    index = user_selected_int + 1

                    # Extract the actual question
                    selected_question = questions_list.splitlines()[index]
                    _, question_item = selected_question.split(': ', 1) # Split at the first ': '

                    # Print the actual question as heading
                    print(Fore.MAGENTA + f'\nYour selected question: {question_item}' + Style.RESET_ALL)

                    # Open the file food_safety_list.csv in read mode in context manager
                    with open('travel_safety_info.csv', encoding="utf-8-sig") as f:
                        # Create a dict object named reader
                        reader = csv.DictReader(f)
                        # Iterate over every row in the file
                        for row in reader:
                            # Check if value in 'Question No.' column matches user's input
                            if int(row['Question No.']) == user_selected_int:
                                # If match found, it extract the information from the current row
                                return [
                                    row['Info 1'],
                                    row['Info 2'],
                                    row['Info 3'],
                                    row['Info 4'],
                                    row['Info 5']
                                ]

                    # If no match found on user entered food, the function returns None
                    return None, None, None, None, None

                # Display the guide for instructions and for quitting the app
                display_guide_on_top() # From print_guide module

                print(Fore.RED + f'Error: "{user_choice}" is invalid. Please enter from 1 to 9.\n' + Style.RESET_ALL)

    except FileNotFoundError:
        print(Fore.RED + 'Error: The travel_safety_info.csv file not found.' + Style.RESET_ALL)
        return None, None, None, None, None
    except Exception as e:
        print(Fore.RED + f'An unexpected error occurred: {e}' + Style.RESET_ALL)
        return None, None, None, None, None
