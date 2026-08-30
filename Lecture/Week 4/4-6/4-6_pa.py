# Kenneth Irving (kenirv5642)
# Date: 08-30-2026
# Description: Program that reads state visit data from a CSV file (Part 1) and displays a vertical bar chart using matplotlib (Part 2).

from datetime import datetime
import csv
from pathlib import Path
import matplotlib.pyplot as plt

# Student ID constant used in chart titles
STUDENT_ID = "kenirv5642"

# Reads the CSV file and prints the output to console for screenshotting. (PT. 1)
def read_csv_file(filePath):
    print("=" * 45)
    print(f'Data Read from {filePath}')
    print("=" * 45)
    
    states = []
    visits = []
    
    with open(filePath, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and len(row) >= 2:
                state = row[0].strip().strip("'\"")
                num_visits = int(row[1].strip())
                states.append(state)
                visits.append(num_visits)
                print(f"State: {state:<18} | Visits: {num_visits}")
                
    print("=" * 45)
    print()
    return states, visits

# Creates and displays a vertical bar chart of states visited using matplotlib. (Pt. 2)
def create_bar_chart(states, visits):
    # Format today's date (e.g., August 30, 2026)
    today_date = datetime.now().strftime("%B %d, %Y")
    
    # Initialize figure
    plt.figure(figsize=(10, 6))
    
    # Plot vertical bars with states on x-axis and visit counts on y-axis
    plt.bar(states, visits, color="skyblue", edgecolor="navy", width=0.6)
    
    # Set title with StudentID and today's date
    plt.title(f"{STUDENT_ID} {today_date} - States Visited", fontsize=14, fontweight="bold")
    
    # Set axis labels
    plt.xlabel("State", fontsize=12)
    plt.ylabel("Number of Visits", fontsize=12)
    
    # Ensure y-axis uses whole number integer increments for visit counts
    max_visits = max(visits) if visits else 5
    plt.yticks(range(0, max_visits + 2))
    
    # Rotate x-axis state labels for readability
    plt.xticks(rotation=45, ha="right")
    
    # Adjust layout to prevent clipping
    plt.tight_layout()
    
    # Display the plot
    plt.show()

# Main function to for reading the CSV file and creating the bar chart.
def main():
    # Construct the file path for the CSV data file in the current directory.
    csv_file_path = Path(__file__).parent / "4-6_pa.csv"
    
    # Read the CSV file, display its contents, and return the states and visit numbers.
    states, visits = read_csv_file(csv_file_path)
    
    # Generate and display the vertical bar chart using the extracted data.
    create_bar_chart(states, visits)


if __name__ == "__main__":
    # Call main function
    main()