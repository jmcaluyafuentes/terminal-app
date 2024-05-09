"""
This module will give information about safe activities for pregnant women.
"""

import csv
from textwrap import dedent
from print_guide import guide, guide_user_response

def check_activities_safety() -> None:
    """
    Discover safe activities for pregnant women from a CSV file.
    """

    activities_safety = True

    while activities_safety:
        # Display the guide for instructions and for quitting the app
        guide() # From print_guide module

        print(dedent('''
        The following are topics about safe activities for pregnant women.\n
        1. Benefits of exercising
        2. Exercises for pregnant women
        3. Activities that can be done outdoors
        '''))

        user_choice = input('Enter your choice (1, 2 or 3): ')

        # Check if user want to view the instructions or exits the app
        guide_user_response(user_choice)

        activity_loop = True

        if user_choice == '1':
            topic = 'Benefits of exercising'
        elif user_choice == '2':
            topic = 'Exercises for pregnant women'
        elif user_choice == '3':
            topic = 'Activities that can be done outdoors'
        else:
            print('Error: Invalid choice. Please enter 1 for Benefits, 2 for Exercises or 3 for Outdoor\n')
            activity_loop = False

        print(f'\n{topic}:')

        while activity_loop:
            # Open the file activities_safety.csv in read mode in context manager
            with open('activities_safety.csv', encoding="utf-8") as f:
                # Create a dict object named reader
                reader = csv.DictReader(f)
                # Iterate over every row in the file
                for row in reader:
                    # Check if the value in 'Topic' column matches the user's entered topic
                    if row['Topic'].lower() == topic.lower():
                        # If match found, it extract the information from the current row
                        infos = [row['Info 1'], row['Info 2'], row['Info 3'], row['Info 4'], row['Info 5']]
                        # Display activities safety information with indices
                        for index, activity_info in enumerate(infos, 1):
                            # Display only if travel info is not an empty string
                            if activity_info:
                                print(f'{index}. {activity_info}')

            activity_loop = False

        activities_safety = get_user_next_action()

def get_user_next_action() -> bool:
    """
    Prompt the user for the next action whether to continue in current sub menu, return to main menu or exit.

    Returns:
        bool: True if user chooses to continue or False if user chooses to return to main menu.
    """
    while True:
        # Prompt the user to get her response
        next_choice = input('\n\nWhat would you like to do next?\n'
                            '1. Continue\n'
                            '2. Return to Safety main menu\n\n'
                            'Enter your choice (1 or 2): ')

        # Check if user want to view the instructions or exits the app
        guide_user_response(next_choice)

        # Check what choice the user selected
        if next_choice == '1':
            return True
        elif next_choice == '2':
            return False
        else:
            # Display the guide for instructions and for quitting the app
            guide() # From print_guide module

            # Inform the user that she entered invalid choice
            print('Invalid choice. Please enter 1 or 2.')

