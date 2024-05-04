from datetime import datetime

def calculate_gestational_age(last_period_date):
    # Get the current date
    current_date = datetime.now()
    print(current_date)

    # Calculate elapsed time from last period to current date in days
    elapsed_time = (current_date - last_period_date).days
    print(elapsed_time)

    # Calculate gestational age in weeks (round down)
    gestational_age_in_weeks = elapsed_time // 7
    print(gestational_age_in_weeks)

last_period_month = int(input('Enter the month of last period: '))
last_period_day = int(input('Enter the day of last period: '))
last_period_year = int(input('Enter the year of last period: '))

last_period_date = datetime(last_period_year, last_period_month, last_period_day)

calculate_gestational_age(last_period_date)