"""
This module is used to check food safety information in CSV file.
"""

import csv

def check_food_safety(food: str) -> tuple[str, str, str]:
    """
    Check the safety information of a certain food during pregnancy from a CSV file.

    Args:
        food (str): The food to be checked for safety.

    Returns:
        tuple[str, str, str]: The safety information of a certain food.
    """

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
                    return (
                        row['Safety Info'],
                        row['Precaution'],
                        row['Food handling']
                    )

        # If no match found on user entered food, the function returns None
        return None, None, None
