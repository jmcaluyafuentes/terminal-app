"""
This module will give information about safe activities for pregnant women.
"""

import csv
from textwrap import dedent
from colorama import Fore, Style
import emoji
from print_guide import display_guide_on_top, guide_user_response
from user_next_action import get_user_next_action

def check_activities_safety() -> None:
    """
    Discover safe activities for pregnant women from a CSV file.
    """

    # Display the guide for instructions and for quitting the app
    display_guide_on_top() # From print_guide module

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
            display_guide_on_top() # From print_guide module

            # Display the error message for invalid user input
            print(Fore.RED + emoji.emojize(dedent(f'''
            :cross_mark: ERROR: "{user_choice}" is an invalid choice.
            Please enter 1 for Benefits, 2 for Exercises or 3 for Outdoor.
            ''')) + Style.RESET_ALL)

            activity_loop = False

        while activity_loop:
            # Print the topic selected by the user
            print(Fore.MAGENTA + f'\n{topic}:' + Style.RESET_ALL)

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
                                    print(Fore.YELLOW + f'{index}. {activity_info}' + Style.RESET_ALL)
            except FileNotFoundError:
                print(Fore.RED + emoji.emojize(':cross_mark: ERROR: File activities_safety.csv not found.') + Style.RESET_ALL)
                break
            except csv.Error as e:
                print(Fore.RED + emoji.emojize(f':cross_mark: ERROR: CSV processing error - {e}') + Style.RESET_ALL)
                break
            except Exception as e:
                print(Fore.RED + emoji.emojize(f':cross_mark: ERROR: An unexpected error occurred: {e}') + Style.RESET_ALL)
                break

            activity_loop = False

            # Ask the user if what she wants to do next
            activities_safety = get_user_next_action() # From user_next_action module

            # Display the guide for instructions and for quitting the app
            display_guide_on_top() # From print_guide module
