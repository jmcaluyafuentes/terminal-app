"""
This module will give information about safe activities for pregnant women.
"""

import csv
from print_guide import guide, guide_user_response

def check_activities_safety() -> None:
    """
    Discover safe activities for pregnant women from a CSV file.
    """

    # Display the guide for instructions and for quitting the app
    guide() # From print_guide module

    activities_safety = True

    while activities_safety:
        print('\nThe following are topics about safe activities for pregnant women.\n')

        # Topics presented in a list
        topics = [
            'Benefits of exercising',
            'Exercises for pregnant women',
            'Activities that can be done outdoors'
        ]

        # Display the topics with indices from the list
        for index, topic in enumerate(topics, 1):
            print(f'{index}. {topic}')

        # Get the user choice
        user_choice = input('\nEnter your choice (1, 2 or 3): ')

        # Check if user want to view the instructions or exits the app
        guide_user_response(user_choice)

        activity_loop = True

        # Identify what topic that the user selected
        if user_choice in ['1', '2', '3']:
            topic = topics[int(user_choice) - 1]
        else:
            # Display the guide for instructions and for quitting the app
            guide() # From print_guide module

            # Display the error message for invalid user input
            print(f'Error: "{user_choice}" is an invalid choice.')
            print('Please enter 1 for Benefits, 2 for Exercises or 3 for Outdoor\n')
            activity_loop = False

        while activity_loop:
            # Print the topic selected by the user
            print(f'\n{topic}:')

            try:
                # Open the file activities_safety.csv in read mode in context manager
                with open('activities_safety.csv', encoding="utf-8") as f:
                    # Create a dict object named reader
                    reader = csv.DictReader(f)
                    # Iterate over every row in the file
                    for row in reader:
                        # Check if the value in 'Topic' column matches the user's entered topic
                        if row['Topic'].lower() == topic.lower():
                            # If match found, extract the information from the current row
                            infos = [
                                row['Info 1'],
                                row['Info 2'],
                                row['Info 3'],
                                row['Info 4'],
                                row['Info 5']
                            ]
                            # Extract the index and value pair in infos list
                            for index, activity_info in enumerate(infos, 1):
                                # Display only if travel info is not an empty string
                                if activity_info:
                                    print(f'{index}. {activity_info}')
            except FileNotFoundError:
                print('Error: File activities_safety.csv not found.')
                break
            except PermissionError as e:
                print(f"Error: Permission denied - {e}")
                break
            except UnicodeDecodeError as e:
                print(f"Error: Unable to decode file - {e}")
                break
            except csv.Error as e:
                print(f"Error: CSV processing error - {e}")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break

            activity_loop = False
            activities_safety = get_user_next_action()
            guide() # From print_guide module

def get_user_next_action() -> bool:
    """
    Prompt the user for the next action whether to continue in current sub menu, 
    return to main menu or exit.

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
            print(f'ERROR: "{next_choice}" is invalid choice. Please enter 1 or 2.')
