from datetime import datetime

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
        return 'first trimester'
    elif 13 <= gestational_age <= 26:
        return 'second trimester'
    else:
        return 'third trimester'

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

    # Display the output
    print(f'You are {gestational_age} weeks pregnant and in {trimester}.')

if __name__ == "__main__":
    main()
