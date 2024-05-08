"""
This module is used to check travel safety information in CSV file.
"""

import csv
from pregnancy_calculator import calculate_gestational_age

def calculate_gestational_age_on_travel(travel_date, last_period_date):
    """
    Calculate the number of weeks pregnant on the planned travel date.

    Args:
        travel_date (datetime.date): The planned travel date.
        last_period_date (datetime.date): The date of last menstrual period.
    
    Returns:
        int: The number of weeks pregnant on the planned travel date.
    """

    # Calculate gestational age in weeks on planned travel date
    gestational_age = calculate_gestational_age(last_period_date)
    weeks_until_travel = (travel_date - last_period_date).days // 7
    weeks_pregnant_on_travel = gestational_age + weeks_until_travel
    return weeks_pregnant_on_travel

def check_travel_safety(travel_date, last_period_date):
    """
    Check the travel information based on the gestational age during the planned travel date.

    Args:
        travel date (datetime.date): Planned travel date.
        last_period_date (datetime.date): Last day of menstrual period

    Returns:
        tuple: The safety information on travel.
    """

    weeks_pregnant_on_travel = calculate_gestational_age_on_travel(travel_date, last_period_date)
    print(f'\nYou are {weeks_pregnant_on_travel} weeks during your planned travel on {travel_date.strftime("%d/%m/%Y")}.')

    if 13 <= weeks_pregnant_on_travel <= 26:
        print('You will be in 2nd trimester and it is safest to travel, provided you are not experiencing any complications.\n')
    else:
        print('Please consult with your doctor, especially if your pregnancy is high risk.\n')

    while True:
        print('The following are possible questions related to travel safety.\n')

        print('Question 1: What are the general considerations when planning to travel?')
        print('Question 2: What are the complications that a pregnant woman encounters?')
        print('Question 3: What are the travel immunization warnings for pregnant women?')
        print('Question 4: What are the risks of long-distance travel during pregnancy?')
        print('Question 5: How to avoid deep vein thrombosis (DVT) when traveling?')
        print('Question 6: What are the considerations in air travel?')
        print('Question 7: What are the considerations when traveling by car?')
        print('Question 8: What are the considerations if traveling in hot weather?')
        print('Question 9: How to avoid food poisoning during travel?\n')

        user_selected = int(input('Please enter the number of your choice: '))

        print('-' * 110)

        while True:

            with open('travel_safety_info.csv', encoding="utf-8-sig") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    if int(row['Question No.']) == user_selected:
                        return [
                            row['Info 1'],
                            row['Info 2'],
                            row['Info 3'],
                            row['Info 4'],
                            row['Info 5']
                        ]

            return (None, None, None, None, None)
