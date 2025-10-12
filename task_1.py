"""
Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
"""

from datetime import datetime

def get_days_from_today(date):
    # parsing the date
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(f"Invalid date format: {date}. Expected YYYY-MM-DD")

    # getting current date
    now = datetime.now().date()

    # return thr  difference, if date is less than today, and if not return 0 
    return (parsed_date - now).days if parsed_date < now else 0


print(get_days_from_today("2020-10-09"))  # -1828 (Current 2025-10-11)  
print(get_days_from_today("2025-10-11"))  # 0 (Current 2025-10-11)
# get_days_from_today("99") # ValueError: Invalid date format: 99. Expected YYYY-MM-DD