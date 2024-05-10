""" 
This module contains the calculations on the information about pregnancy such as
gestational age in weeks, trimester, estimated due date (EDD) and countdown until EDD.
"""

from datetime import datetime, date, timedelta


def calc_pregnancy_info(last_period_date: date) -> tuple[int, str, date, int, int]:
    """
    Calculate and display the information about pregnancy such as gestational age
    in weeks, trimester, estimated due date (EDD) and countdown until EDD.

    Args:
        last_period_date (date): The last menstrual period date.

    Returns:
        tuple[int, str, date, int, int]: Gestational age in weeks, trimester, due date, countdown weeks remaining, countdown days remaining.
    """
    # Calculate gestational age in weeks
    gestational_age = calc_gestational_age(last_period_date)

    # Calculate trimester based on gestational age
    trimester = calc_trimester(gestational_age)

    # Calculate estimated due date
    due_date = calc_due_date(last_period_date)

    # Calculate the countdown from current date until due date
    weeks_remaining, days_remaining = calc_countdown(due_date)

    return gestational_age, trimester, due_date, weeks_remaining, days_remaining


def calc_gestational_age(last_period_date: date) -> int:
    """
    Calculate gestational age in weeks by subtracting current date and last menstrual period.

    Args:
        last_period_date (date): The date of last menstrual period.

    Returns:
        int: The gestational age in weeks.
    """
    # Get the current date
    current_date = date.today()

    # Calculate elapsed time from last period to current date in days
    elapsed_time = (current_date - last_period_date).days

    # Calculate gestational age in weeks and round down the result
    gestational_age_in_weeks = elapsed_time // 7

    return gestational_age_in_weeks


def calc_trimester(gestational_age: int) -> str:
    """
    Determine the trimester based on the gestational age.

    Args:
        gestational_age (int): The gestational age in weeks.

    Returns:
        str: The first, second or third trimester.
    """

    # Check what trimester range the gestational age fall
    if gestational_age <= 12:
        return "First trimester"
    elif 13 <= gestational_age <= 26:
        return "Second trimester"
    else:
        return "Third trimester"


def calc_due_date(last_period_date: date) -> date:
    """
    Calculate the due date by adding 40 weeks to the date of last menstrual period.

    Args:
        last_period_date (date): The date of last menstrual period.

    Returns:
        date: The estimated due date.
    """

    # Calculate the due date by adding 40 weeks to the last menstrual period date
    estimated_due_date = last_period_date + timedelta(weeks=40)
    return estimated_due_date


def calc_countdown(due_date: date) -> tuple[int, int]:
    """
    Calculate the countdown from current date until the due date.

    Args:
        due_date (date): The estimated due date.

    Returns:
        tuple [int, int]: Remaining numbers of weeks and days until due date
    """

    # Get the current date
    current_date = date.today()

    # Calculate the difference in days between due date and current date
    days_to_due_date = (due_date - current_date).days

    # Calculate weeks and days remaining
    weeks_remaining = days_to_due_date // 7
    days_remaining = days_to_due_date % 7

    return weeks_remaining, days_remaining
