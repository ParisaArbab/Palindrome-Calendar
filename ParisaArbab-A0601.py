"""
Author: Parisa Arbab
Date: Feb 19 2024
Statement:“I have not given or received any unauthorized assistance on this assignment.”
YouTube Link:https://youtu.be/L9ZhCNcFNV0

Explained in the above link:
1. How did you iterate through the different dates?
2. How did you test if a date was a palindrome date?
3. Where you able to ignore entire months or even years without evaluating every date?
"""


def is_palindrome(s):   #answer to question 2
    """Check if a string is a palindrome."""
    return s == s[::-1]

def generate_palindrome_dates():
    """Generate palindrome dates in the 21st century (2001-2100) in DD/MM/YYYY format."""
    palindrome_dates = []
    for year in range(2001, 2101):
        # The first two digits of the year must match the last two digits of the day
        for month in range(1, 13):   #answer to question 1
            for day in range(1, 32):
                if month == 2 and day > 28:
                    continue  # Skip invalid dates in February
                if month in [4, 6, 9, 11] and day > 30:
                    continue  # Skip invalid dates in April, June, September, November

                # Format the date in DD/MM/YYYY format
                date_str = f"{day:02}/{month:02}/{year}"
                # Check if the date string is a palindrome
                if is_palindrome(date_str.replace('/', '')):
                    palindrome_dates.append(date_str)
    return palindrome_dates

# Generate the palindrome dates
palindrome_dates = generate_palindrome_dates()

# Now, let's write these dates to a file
with open('C:/Users/parsu/PycharmProjects/DSC430/palindrome_dates.txt', 'w') as file:
    for date in palindrome_dates:
        file.write(date + '\n')

# # Indicate the completion and the number of dates found
# len(palindrome_dates), "Palindrome dates written to file."
# # Re-defining the necessary parts to print the file path, as the code execution state was reset.

# Path to the file containing the palindrome dates
file_path = 'C:/Users/parsu/PycharmProjects/DSC430/palindrome_dates.txt'
print(f"Find the file 'palindrome_dates.txt' in this path: {file_path}")
