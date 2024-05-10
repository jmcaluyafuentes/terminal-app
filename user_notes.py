"""
This module will accept user input and record personal notes with date and time stamps.
"""

from datetime import datetime
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
            note = input('\nEnter your note: ')

            # Check if user want to view the instructions or exits the app
            instructions = guide_user_response(note)

            if not instructions:
                # Generate a timestamp in DD/MM/YYYY format
                timestamp = datetime.now().strftime("%d-%m-%y %H:%M:%S")

                # Open the notes file in append mode
                with open('personal_notes.txt', 'a', encoding="utf-8-sig") as f:
                    # Write the note to the file with timestamp
                    f.write(f'{timestamp}: {note}\n')

                print('Remarks: Note recorded successfully.')

                record = get_user_next_action()

        except Exception as e:
            print(f'An error occurred: {e}')

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
                    print('No notes found.')
                else:
                    print('Recorded Notes:')
                    for line in lines:
                        # Split each line into timestamp and note
                        parts = line.strip().split(': ', 1)
                        if len(parts) == 2:
                            timestamp, note = parts
                            print(f'{timestamp}: {note}')

                display = get_user_next_action()

        except FileNotFoundError:
            print('Error: File not found. Please try option 1 to write your first note.')
        except Exception as e:
            print(f'An error occurred: {e}')

        # Display the guide for instructions and for quitting the app
        display_guide_on_top() # From print_guide module
