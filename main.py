from datetime import datetime
from pregnancy_calculator import (
    calculate_gestational_age,
    calculate_trimester,
    calculate_due_date,
    calculate_countdown
)

# Main function
def main():
    """
    Main function to get user input, calculate and display the information about pregnancy such as
    gestational age in weeks, trimester, estimated due date (EDD) and countdown until EDD.
    """

    # Prompt the user to enter the month, day and year of her last menstrual period
    last_period_month = int(input('Enter the month of last period: '))
    last_period_day = int(input('Enter the day of last period: '))
    last_period_year = int(input('Enter the year of last period: '))
    last_period_date = datetime(last_period_year, last_period_month, last_period_day).date()

    # Calculate gestational age in weeks
    gestational_age = calculate_gestational_age(last_period_date)

    # Calculate trimester based on gestational age
    trimester = calculate_trimester(gestational_age)

    # Calculate estimated due date
    due_date = calculate_due_date(last_period_date)

    # Calculate the countdown from current date until due date
    weeks_remaining, days_remaining = calculate_countdown(due_date)

    # Display relevant information about the pregnancy
    print(f'You are {gestational_age} weeks pregnant.')
    print(f'Trimester: {trimester}')
    print(f"Estimated Due Date: {due_date.strftime('%d/%m/%Y')}")
    print(f'You are {weeks_remaining} week(s) and {days_remaining} day(s) until due date.')

if __name__ == "__main__":
    main()
