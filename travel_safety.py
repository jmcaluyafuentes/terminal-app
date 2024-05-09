"""
This module is used to check travel safety information in CSV file.
"""

import csv
from textwrap import dedent
from datetime import datetime, date
from print_guide import guide_user_response

def calculate_gestational_age_on_travel(travel_date: datetime.date, last_period_date:datetime.date) -> int:
    """
    Calculate the number of weeks pregnant on the planned travel date.

    Args:
        travel_date (datetime.date): The planned travel date.
        last_period_date (datetime.date): The date of last menstrual period.
    
    Returns:
        int: The number of weeks pregnant on the planned travel date.
    """

    # Get the current date
    current_date = date.today()

    # Calculate elapsed time from last period to current date in days
    elapsed_time = (current_date - last_period_date).days

    # Calculate gestational age in weeks and round down the result
    gestational_age_in_weeks = elapsed_time // 7

    # Calculate the number of weeks from current date to the travel date
    weeks_until_travel = (travel_date - last_period_date).days // 7

    # Calculate the gestational age (in weeks) on the planned travel date
    weeks_pregnant_on_travel = gestational_age_in_weeks + weeks_until_travel

    return weeks_pregnant_on_travel

def check_travel_safety(travel_date: datetime.date, last_period_date: datetime.date) -> tuple[str, str, str, str, str]:
    """
    Check the travel information based on the gestational age during the planned travel date.

    Args:
        travel date (datetime.date): Planned travel date.
        last_period_date (datetime.date): Last day of menstrual period

    Returns:
        tuple[str, str, str, str, str]: Several safety information about travel.
    """
    # Calculate the gestational age (in weeks) on the planned travel date
    weeks_pregnant_on_travel = calculate_gestational_age_on_travel(travel_date, last_period_date)

    # Display to user the gestational age (in weeks) on the planned travel date
    print('\nGeneral Information:')
    print(f'\nYou are {weeks_pregnant_on_travel} weeks during your planned travel on {travel_date.strftime("%d/%m/%Y")}.')

    # Check if user is on 2nd semester on planned travel date. 2nd semester is the safest to travel.
    if 13 <= weeks_pregnant_on_travel <= 26:
        print('You will be in 2nd trimester and it is safest to travel, provided you are not experiencing any complications.\n')
    else:
        print('Please consult with your doctor, especially if your pregnancy is high risk.\n')

    while True:
        # Give the user the list of questions as a guide
        print(dedent('''The following are possible questions related to travel safety.\n
        Question 1: What are the general considerations when planning to travel?
        Question 2: What are the complications that a pregnant woman encounters?
        Question 3: What are the travel immunization warnings for pregnant women?
        Question 4: What are the risks of long-distance travel during pregnancy?
        Question 5: How to avoid deep vein thrombosis (DVT) when traveling?
        Question 6: What are the considerations in air travel?
        Question 7: What are the considerations when traveling by car?
        Question 8: What are the considerations if traveling in hot weather?
        Question 9: How to avoid food poisoning during travel?\n
        '''))

        # Prompt the user what question she would like an answer about the travel information
        user_selected = input('Please enter the number of your choice: ')

        # Check if user want to view the instructions or exits the app
        instructions = guide_user_response(user_selected)

        while not instructions:
            # Open the file food_safety_list.csv in read mode in context manager
            with open('travel_safety_info.csv', encoding="utf-8-sig") as f:
                # Create a dict object named reader
                reader = csv.DictReader(f)
                # Iterate over every row in the file
                for row in reader:
                    # Check if the value in 'Question No.' column matches the user's entered question number
                    if int(row['Question No.']) == int(user_selected):
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
