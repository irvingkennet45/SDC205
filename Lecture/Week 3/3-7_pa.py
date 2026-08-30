# Kenneth Irving (kenirv5642)
# Date: 08-30-2026
# Description: Program that creates and displays a DataFrame of ballroom capacities, plots a vertical bar graph of capacities, and generates a pie chart of attendee demographics.

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Student ID constant
STUDENT_ID = "kenirv5642"


def main():
    # Print Student ID
    print(STUDENT_ID)
    
    # Define ballroom capacity data
    capacity_data = {
        "Names": ["Ballroom 1", "Ballroom 2", "Ballroom 3"],
        "Capacity": [25000, 11000, 5000]
    }
    
    # Create and print the table showing ballroom capacities as a DataFrame
    capacity_df = pd.DataFrame(capacity_data)
    print(capacity_df)
    
    # Format today's date for chart titles
    today_date = datetime.now().strftime("%B %d, %Y")
    
    # Print/Display a vertical bar graph showing the capacity of each ballroom
    plt.figure(figsize=(8, 6))
    plt.bar(capacity_df["Names"], capacity_df["Capacity"], color=["royalblue", "cornflowerblue", "lightsteelblue"], edgecolor="black", width=0.5)
    plt.title(f"{STUDENT_ID} {today_date} - Ballroom Capacities", fontsize=14, fontweight="bold")
    plt.xlabel("Ballroom", fontsize=12)
    plt.ylabel("Capacity (Number of People)", fontsize=12)
    plt.ylim(0, 30000)
    
    # Add data labels on top of each bar
    for i, v in enumerate(capacity_df["Capacity"]):
        plt.text(i, v + 500, f"{v:,}", ha="center", fontweight="bold")
        
    plt.tight_layout()
    plt.show()  # Close the bar graph window to allow the pie chart to display
    
    # Define demographics data for attendees
    demographics_labels = ["Children", "Adults", "Teens"]
    demographics_counts = [18000, 13000, 10000]
    colors = ["#ff9999", "#66b3ff", "#99ff99"]
    
    # Print/Display a pie chart for the breakdown of event attendee demographics
    plt.figure(figsize=(8, 6))
    plt.pie(
        demographics_counts, 
        labels=demographics_labels, 
        autopct="%1.1f%%", 
        startangle=140, 
        colors=colors,
        wedgeprops={"edgecolor": "black", "linewidth": 1}
    )
    plt.title(f"{STUDENT_ID} {today_date} - Attendee Demographics", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

