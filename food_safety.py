"""
This module is used to check food safety
"""

import csv

def check_food_safety(food):
    """
    Check the safety information of a certain food during pregnancy from a CSV file.

    Args:
        food (str): The food to be checked for safety.

    Returns:
        str: The safety information of a certain food.
    """

    with open('food_safety_list.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Food'].lower() == food.lower():
                return row['Safety Info']

    return 'Safety information is not available for this food.'