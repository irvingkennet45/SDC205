from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Student ID constant used in chart titles
STUDENT_ID = "kenirv5642"
print(STUDENT_ID)


def main():
    # Store a classroom roster of 10 students in a NumPy array
    students = np.array([
        "Alice", "Bob", "Charlie", "David", "Emma",
        "Frank", "Grace", "Hannah", "Ian", "Jack"
    ])
    
    # Define two different subjects for the grades
    subjects = ["Math", "Science"]
    
    # Create a hierarchical index for the student and subject using the MultiIndex function
    multi_index = pd.MultiIndex.from_product(
        [students, subjects], 
        names=["Student", "Subject"]
    )
    
    # Define grade data for each student across both subjects (10 students x 2 subjects = 20 grades)
    grades = [
        88, 92,  # Alice: Math, Science
        79, 85,  # Bob: Math, Science
        95, 90,  # Charlie: Math, Science
        70, 78,  # David: Math, Science
        91, 94,  # Emma: Math, Science
        83, 80,  # Frank: Math, Science
        89, 96,  # Grace: Math, Science
        76, 82,  # Hannah: Math, Science
        94, 88,  # Ian: Math, Science
        85, 87   # Jack: Math, Science
    ]
    
    # Create a Dataframe of grades indexed by the student and subject
    df = pd.DataFrame(grades, index=multi_index, columns=["Grade"])
    
    # Display the Dataframe to the console
    print("=" * 45)
    print("Classroom Grades Datatable:")
    print("=" * 45)
    print(df)
    print("=" * 45)
    print()
    
    # Group by the 'Subject' level and calculate the mean grade for each subject
    subject_mean = df.groupby(level="Subject")["Grade"].mean()
    
    # Display the calculated subject mean results
    print("Mean Grade Grouped by Subject:")
    print(subject_mean)
    print()
    
    # Create and display a vertical bar graph of the subject mean grades using matplotlib
    plt.figure(figsize=(8, 6))
    
    # Plot vertical bars representing the mean of each subject
    plt.bar(subject_mean.index, subject_mean.values, color=["skyblue", "lightcoral"], edgecolor="navy", width=0.4)
    
    # Format today's date (e.g., August 30, 2026)
    today_date = datetime.now().strftime("%B %d, %Y")
    
    # Set the title of the chart including StudentID and today's date
    plt.title(f"{STUDENT_ID} {today_date} - Mean Grade by Subject", fontsize=14, fontweight="bold")
    
    # Set axis labels and axis limits
    plt.xlabel("Subject", fontsize=12)
    plt.ylabel("Mean Grade", fontsize=12)
    plt.ylim(0, 100)
    
    # Add numerical labels above each bar
    for i, v in enumerate(subject_mean.values):
        plt.text(i, v + 1.5, f"{v:.2f}", ha="center", fontweight="bold", fontsize=11)
        
    # Adjust layout to prevent clipping
    plt.tight_layout()
    
    # Display the vertical bar graph
    plt.show()


if __name__ == "__main__":
    # Execute the main function
    main()

