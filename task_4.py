from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "198501.03"},
    {"name": "Jane Smith", "birthday": "1990.12.30"},
    {"name": "Sam Neil", "birthday": "1985.10.19"},
    {"name": "Jack Taylor", "birthday": "1990.10.12"},
]


def get_upcoming_birthdays(users):
    result = []
    current_year = datetime.now().year
    # today = datetime(2025, 12, 29).date()  # Example for New year
    today = datetime.today().date()
    next_week = today + timedelta(days=7)


    for user in users:
        # The original birthday
        # birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        try:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except ValueError:
            print(f"Time data {user["birthday"]} for {user["name"]} does not match")
            continue

        # Create birthday for current year
        birthday_this_year = datetime(current_year, birthday.month, birthday.day).date()

        # Check if birthday already passed, move to next year
        if birthday_this_year < today:
            birthday_this_year = datetime(current_year + 1, birthday.month, birthday.day).date()

        # Check if day is weekend
        is_weekend = birthday_this_year.weekday() >= 5

        if today <= birthday_this_year <= next_week:
            # Shift to next Monday if on weekend
            if is_weekend:
                birthday_this_year += timedelta(
                    days=(7 - birthday_this_year.weekday()) % 7
                )
            
            result.append(
                {
                    "name": user["name"],
                    "congratulation_date": birthday_this_year.strftime("%Y.%m.%d"),
                }
            )

    return result


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
