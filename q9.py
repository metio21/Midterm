def days_since_birthday(birthday):
    """
    :param birthday: user's birthday
    :return: total days passed from when user was born
    """
    # splits birthday into day, month, and year (we only need the year here).
    parts = birthday.split("-")
    birth_year = int(parts[2])

    #ask the user to input the current year.
    current_year = int(input("Enter the current year: "))

    total_days = 0  # Initialize a counter for the total number of days.

    # Loop through each full year between the year after the birth year and the year before the current year.
    for year in range(birth_year + 1, current_year):
        # Check if the year is a leap year.
        # A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            total_days += 366
        else:
            total_days += 365

    # returns the total days in all the full years.
    return total_days


# Example usage:
print(days_since_birthday("21-05-2005")) #my birthday
