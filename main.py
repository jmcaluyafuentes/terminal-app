from datetime import datetime, timedelta

def calculate_gestational_age(last_period_date):

    # Get the current date
    current_date = datetime.now()

    # Calculate elapsed time from last period to current date in days
    elapsed_time = (current_date - last_period_date).days

    # Calculate gestational age in weeks and round down the result
    gestational_age_in_weeks = elapsed_time // 7

    return gestational_age_in_weeks

def calculate_trimester(gestational_age):
    if gestational_age <= 12:
        return 'First trimester'
    elif 13 <= gestational_age <= 26:
        return 'Second trimester'
    else:
        return 'Third trimester'

def calculate_due_date(last_period_date):
    estimated_due_date = last_period_date + timedelta(weeks=40)
    return estimated_due_date

def calculate_countdown(due_date):
    # Get the current date
    current_date = datetime.now()

    # Calculate the difference in days between due date and current date
    days_to_due_date = (due_date - current_date).days

    # Calculate weeks and days remaining
    weeks_remaining = days_to_due_date // 7
    days_remaining = days_to_due_date % 7

    return weeks_remaining, days_remaining

# Main function
def main():

    # Prompt the use to enter the month, day and year of her last period
    last_period_month = int(input('Enter the month of last period: '))
    last_period_day = int(input('Enter the day of last period: '))
    last_period_year = int(input('Enter the year of last period: '))
    last_period_date = datetime(last_period_year, last_period_month, last_period_day)

    # Calculate gestational age in weeks
    gestational_age = calculate_gestational_age(last_period_date)

    # Calculate trimester based on gestational age
    trimester = calculate_trimester(gestational_age)

    # Calculate estimated due date
    due_date = calculate_due_date(last_period_date)

    # Calculate countdown from current date until due date
    weeks_remaining, days_remaining = calculate_countdown(due_date)

    # Display the output
    print(f'You are {gestational_age} weeks pregnant.')
    print(f'Trimester: {trimester}')
    print(f"Estimated Due Date: {due_date.strftime('%d/%m/%Y')}")
    print(f'You are {weeks_remaining} week(s) and {days_remaining} day(s) until due date.')

if __name__ == "__main__":
    main()
