# Kenneth Irving (kenirv5642)
# Date: 08-30-2026
# Description: This program provides a menu for automating Excel spreadsheet tasks.
from datetime import datetime

print("kenirv5642's Excel Spreadsheet Automation Menu")

# Store the possible menu options in a list
menuOptions = [
    "Input Data",
    "View Current Data",
    "Generate Report"
]

print("Choose a number from the following options:")
# Loop through menu options and print them to the console
for index, option in enumerate(menuOptions, start=1):
    print(f"{index}. {option}")

# Retrieve user choice
userChoice = int(input("\nEnter your choice: "))

# Using if-else statement to determine if user input is a valid menu option
if 1 <= userChoice <= len(menuOptions):
    print(f"You selected {userChoice} at", str(datetime.now()))
else:
    print("Error: Invalid choice selected.")