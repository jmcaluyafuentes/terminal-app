"""
This module will ask the user if what she wants to do next.
"""

from print_guide import display_guide_on_top, guide_user_response

def get_user_next_action() -> bool:
    """
    Prompt the user for the next action whether to continue in current menu or
    go back to one menu up.

    Returns:
        bool: True if user chooses to continue or False if user chooses to return to main menu.
    """
    user_next_action = True

    while user_next_action:
        user_choice = True

        # Prompt the user to get her response
        next_choice = input('\nWhat would you like to do next?\n'
                            '1. Continue\n'
                            '2. Go back one menu up\n\n'
                            'Enter your choice (1 or 2): ')

        # Check if user want to view the instructions or exits the app
        instructions = guide_user_response(next_choice)

        while not instructions:
            # Check what choice the user selected
            if next_choice == '1':
                user_next_action = False
            elif next_choice == '2':
                user_choice = False
                user_next_action = False
            else:
                # Display the guide for instructions and for quitting the app
                display_guide_on_top() # From print_guide module

                # Inform the user that she entered invalid choice
                print(f'"{next_choice}" is an invalid choice. Please enter 1 or 2.\n')
            instructions = True

    return user_choice
