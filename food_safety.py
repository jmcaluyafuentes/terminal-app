"""
This module is used to check food safety information in CSV file.
"""

import csv
from print_guide import display_guide_on_top

def check_food_safety(food: str) -> tuple[str, str, str]:
    """
    Check the safety information of a certain food during pregnancy from a CSV file.

    Args:
        food (str): The food to be checked for safety.

    Returns:
        tuple[str, str, str]: The safety information of a certain food.
    """

    food_safety_infos = None, None, None

    while True:
        # Open the file food_safety_list.csv in read mode in context manager
        with open('food_safety_list.csv', encoding="utf-8") as f:
            # Create a dict object named reader
            reader = csv.DictReader(f)
            # Iterate over every row in the file
            for row in reader:
                # Check if the value in 'Food' column matches the user's entered food
                if row['Food'].lower() == food.lower():
                    # If match found, it extract the information from the current row
                    food_safety_infos = (
                        row['Safety Info'],
                        row['Precaution'],
                        row['Food handling']
                    )
        break

    # Display the guide for instructions and for quitting the app
    display_guide_on_top() # From print_guide module

    return food_safety_infos
