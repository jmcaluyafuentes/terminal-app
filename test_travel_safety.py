"""
This module will test the travel_safety module
"""

from datetime import datetime
from travel_safety import calc_gestational_age_on_travel

def test_valid_dates():
    """
    Test if user entered valid date
    """
    test1 = 24
    user_input_travel_date = '6/6/2024'
    user_input_last_period_date = '26/2/2024'
    travel_date = datetime.strptime(user_input_travel_date, '%d/%m/%Y').date()
    last_period_date = datetime.strptime(user_input_last_period_date, '%d/%m/%Y').date()
    assert calc_gestational_age_on_travel(travel_date, last_period_date) == test1

    test2 = 31
    user_input_travel_date = '14/7/2024'
    user_input_last_period_date = '20/2/2024'
    travel_date = datetime.strptime(user_input_travel_date, '%d/%m/%Y').date()
    last_period_date = datetime.strptime(user_input_last_period_date, '%d/%m/%Y').date()
    assert calc_gestational_age_on_travel(travel_date, last_period_date) == test2
