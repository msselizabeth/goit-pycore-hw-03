"""
Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
"""

from datetime import datetime


def get_days_from_today(date):
    try:
        # parsing the date
        parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print(f"Invalid date format: {date}. Expected YYYY-MM-DD")
        return None
    
    # getting current date
    now = datetime.now().date()

    return (parsed_date - now).days


print(get_days_from_today("2020-10-09"))
print(get_days_from_today("2025-10-11"))
print(get_days_from_today("2025-10-30"))
print(get_days_from_today("2025.10.10"))
