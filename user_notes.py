"""
This module will accept user input and record personal notes with date and time stamps.
"""

import sys
from datetime import datetime
from colorama import Fore, Style
import emoji
from print_guide import display_guide_on_top, guide_user_response
from user_next_action import get_user_next_action

def record_personal_notes() -> None:
    """
    Record a personal note with timestamp and append it to a text file.
    """
    record = True
    while record:
        try:
            # Display the guide for instructions and for quitting the app
            display_guide_on_top() # From print_guide module

            # Get user input for the note
            user_note = input('\nEnter your note: ')

            # Check if user want to view the instructions or exits the app
            instructions = guide_user_response(user_note)

            if not instructions:
                # Generate a timestamp in DD/MM/YYYY format
                timestamp = datetime.now().strftime("%d-%m-%y %H:%M:%S")

                # Open the notes file in append mode
                with open('personal_notes.txt', 'a', encoding="utf-8-sig") as f:
                    # Write the note to the file with timestamp
                    f.write(f'{timestamp}: {user_note}\n')

                print(Fore.YELLOW + 'Remarks: Note recorded successfully.' + Style.RESET_ALL)

                # Ask user if what she wants to do next
                record = get_user_next_action() # From user_next_action module

        except KeyboardInterrupt:
            print(Fore.RED + emoji.emojize('\n:cross_mark: ERROR: Keyboard interrupt received. Sorry, your last note was not saved.') + Style.RESET_ALL)
            sys.exit(1)
        # Catch any other unexpected exceptions
        except Exception as e:
            print(Fore.RED + emoji.emojize(f':cross_mark: ERROR: An unexpected error occurred: {e}') + Style.RESET_ALL)

        # Display the guide for instructions and for quitting the app
        display_guide_on_top() # From print_guide module

def display_personal_notes() -> None:
    """
    Display all recorded personal notes with timestamp from the note file.
    """
    # Display the guide for instructions and for quitting the app
    display_guide_on_top() # From print_guide module

    display = True
    while display:
        try:
            # Open the notes file in read mode
            with open('personal_notes.txt', 'r', encoding="utf-8-sig") as f:
                # Read all lines from the file
                lines = f.readlines()
                # Check if there are recorded notes
                if not lines:
                    print(Fore.RED + 'No notes found.' + Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + 'YOUR RECORDED NOTES:' + Style.RESET_ALL)
                    for line in lines:
                        # Split each line into timestamp and note
                        parts = line.strip().split(': ', 1)
                        if len(parts) == 2:
                            timestamp, note = parts
                            print(Fore.YELLOW + f'{timestamp}: {note}' + Style.RESET_ALL)

                # Ask user if what she wants to do next
                display = get_user_next_action() # From user_next_action module

        except FileNotFoundError:
            print(Fore.RED + emoji.emojize(':cross_mark: ERROR: File not found. Please try option 1 to write your first note.') + Style.RESET_ALL)
            return None
        except KeyboardInterrupt:
            print(Fore.RED + emoji.emojize('\n:cross_mark: ERROR: Keyboard interrupt received.') + Style.RESET_ALL)
            sys.exit(1)
        # Catch any other unexpected exceptions
        except Exception as e:
            print(Fore.RED + emoji.emojize(f':cross_mark: ERROR: An unexpected error occurred: {e}') + Style.RESET_ALL)

        # Display the guide for instructions and for quitting the app
        display_guide_on_top() # From print_guide module
