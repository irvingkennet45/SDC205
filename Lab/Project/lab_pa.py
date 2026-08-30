# Kenneth Irving (kenirv5642)
# Date: 08-30-2026
# Description: This program provides a menu for automating Excel spreadsheet tasks.

from datetime import datetime
# As far as I can tell, I'm allowed to use other modules.
from pathlib import Path
from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, Reference

# Function to convert numerical data based on selected spreadsheet option
def convertData(data):
    if userChoice == 1:
        return (data - 32) * 5 / 9      # F to C
    elif userChoice == 2:
        return data / 2.205             # lbs. to kg.
    elif userChoice == 3:
        return data * 2.54              # in. to cm.
    else:
        return data

# Function to insert/append comma-separated data into a CSV file with error handling
def insertData(filePath, dataString):
    try:
        # Open file with append permissions ('a'), creating it if it does not exist
        with open(filePath, 'a') as file:
            file.write(dataString + "\n")
        return True
    except Exception as e:
        print(f"Error writing to file '{filePath}': {e}")
        return False

# Function to display the contents and path of a CSV file using read permissions ('r') with error handling
def viewData(filePath):
    try:
        print('')
        print("=" * 50)
        print(f"Path of the file being read: {filePath}")
        print("=" * 50)
        print("  -------------------- SOF ---------------------")
        with open(filePath, 'r') as file:
            contents = file.read()
            print(contents)
        print("  -------------------- EOF ---------------------")
    except Exception as e:
        print(f"Error reading file '{filePath}': {e}")

# Function to get user entries, convert data, and store each entry into ZooData.csv
def getInput():
    try:
        numEntries = int(input("How many entries are you inputting? "))
        print('')
        for i in range(numEntries):
            # Header/Border for each entry
            print(('=' * 50))

            entryDate = input("Enter a date: ")
            if userChoice == 1:
                val = float(input("Enter the highest temp for the inputted date (in F): "))

            # From the way I read the instructions, this is only needed for
            # the people that chose to do a weight or rainfallspreadsheet
            # instead of temperature, but I added it just in case I'm wrong.
            elif userChoice == 2:   
                val = float(input("Enter the weight in lbs for the inputted date: "))
            elif userChoice == 3:
                val = float(input("Enter the rain amount in inches for the inputted date: "))

            # Exit the program if the user selects an invalid menu option
            else:
                exit("Error: Invalid menu option selected. Exiting program...")
            
            # Function: convertData
            # Argument Req.: data (numerical value to be converted)
            # Expected Return Value: converted numerical value as a float
            convertedVal = convertData(val)
            
            # Create comma-separated data string
            dataString = f"{entryDate},{val},{convertedVal}"
            
            # Store the entry into ZooData.csv using insertData function
            csvPath = "ZooData.csv"
            writeSuccess = insertData(csvPath, dataString)
            
            if writeSuccess:
                print(f"\nThe following data was saved at {datetime.now()}: {dataString}.")
    except Exception as e:
        print(f"Error processing input: {e}")

# Function: createChart
# Arguements Req.: filePath (path to the CSV data file), chartType (type of chart to create: 'line' or 'bar')
# Argument Types: filePath (str or Path), chartType (str)
# Expected Return Value: None (creates and saves chart in final.xlsx)
def createChart(filePath, chartType):
    try:
        # Ask the user to choose data source
        print("\nChoose data source for the chart:")
        print("1. Initial Data (Fahrenheit)")
        print("2. Converted Data (Celsius)")
        sourceChoice = int(input("\nEnter choice (1 or 2): "))

        # Open the CSV file and extract data with type casting
        rows = []
        with open(filePath, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) >= 3:
                        entryDate = parts[0].strip()
                        initialVal = float(parts[1].strip())
                        convertedVal = float(parts[2].strip())
                        rows.append([entryDate, initialVal, convertedVal])

        if not rows:
            print("Error: No data found in the CSV file.")
            return

        # Using openpyxl, create workbook and write data
        wb = Workbook()
        ws = wb.active
        ws.title = "ZooData"

        # Append headers
        ws.append(["Date", "Initial Data", "Converted Data"])

        # Append data rows
        for row in rows:
            ws.append(row)

        # Select data column and axis title based on user selection
        if sourceChoice == 1:
            valCol = 2
            yAxisTitle = "Initial Value (F)"
        elif sourceChoice == 2:
            valCol = 3
            yAxisTitle = "Converted Value (C)"
        else:
            print("Invalid choice. Defaulting to initial data.")
            valCol = 2
            yAxisTitle = "Initial Value (F)"

        # Define data and categories references
        dataRef = Reference(ws, min_col=valCol, min_row=1, max_row=len(rows) + 1)
        catsRef = Reference(ws, min_col=1, min_row=2, max_row=len(rows) + 1)

        # Instantiate chart based on chartType argument
        if chartType.lower() == 'bar':
            chart = BarChart()
            chart.type = "col"
            chart.style = 10
        else:
            chart = LineChart()
            chart.style = 13

        # Configure chart title and axis labels (<student ID> <current date>)
        studentID = "kenirv5642"
        currentDate = datetime.now().strftime("%m/%d/%Y")
        chart.title = f"{studentID} {currentDate}"
        chart.x_axis.title = "Date"
        chart.y_axis.title = yAxisTitle

        chart.add_data(dataRef, titles_from_data=True)
        chart.set_categories(catsRef)

        # Place chart on worksheet
        ws.add_chart(chart, "E2")

        # Save spreadsheet titled final.xlsx
        outputFilePath = Path(filePath).parent / "final.xlsx"
        wb.save(outputFilePath)
        print(f"\nReport successfully generated and saved to '{outputFilePath}'")
    except Exception as e:
        print(f"Error creating chart: {e}")

# Function: generateReport
# Arguments Req.: filePath (path to the CSV data file)
# Argument Types: filePath (str or Path)
# Expected Return Value: None (prompts user for chart type and calls createChart)
def generateReport(filePath):
    try:
        print("\nChoose a chart type to generate:")
        print("1. Line Chart")
        print("2. Bar Chart")
        chartChoice = input("Enter choice (1 for Line, 2 for Bar, or 'line'/'bar'): ").strip().lower()

        if chartChoice in ['1', 'line']:
            chartType = 'line'
        elif chartChoice in ['2', 'bar']:
            chartType = 'bar'
        else:
            print("Invalid chart choice. Defaulting to line chart.")
            chartType = 'line'

        createChart(filePath, chartType)
    except Exception as e:
        print(f"Error generating report: {e}")

print("kenirv5642's Excel Spreadsheet Automation Menu\n")

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

print('')

# Call 'getInput' if option 1 was selected, 'viewData' if option 2 was selected, 'generateReport' if option 3 was selected; otherwise, print an error message
if userChoice == 1:
    getInput()
elif userChoice == 2:
    ZooDataFilePath = Path(__file__).parent / "ZooData.csv"
    viewData(ZooDataFilePath)
elif userChoice == 3:
    ZooDataFilePath = Path(__file__).parent / "ZooData.csv"
    generateReport(ZooDataFilePath)
else:
    print("Error: The chosen functionality is not implemented yet")