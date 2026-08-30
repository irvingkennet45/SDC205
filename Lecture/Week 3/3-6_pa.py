# Kenneth Irving (kenirv5642)
# Date: 08-30-2026
# Description: Demonstrates function definitions, passing parameters, returning values, and calling functions from main().

# Define global student ID
studentId = "kenirv5642"

# Prints the student ID to the console. Takes no parameters and returns no value.
def functionOne():
    print(f"My Student ID is {studentId}")

# Prompts the user for two numbers, calculates and prints their sum, and returns the sum to 'main()'.
def functionTwo():
    numOne = int(input("Please enter a number: "))
    numTwo = int(input("Please enter a number: "))
    sumResult = numOne + numTwo
    print(f"The sum of {numOne} and {numTwo} is {sumResult}.")
    return sumResult

# Evaluates whether the sum is greater than 5 or not, prints the message, and returns the numeric part of the Student ID.
def functionThree(calculatedSum):

    if calculatedSum > 5:
        print("The sum is greater than 5.")
    else:
        print("The sum is 5 or less.")

    # Last 4 digits of the student ID are returned as an integer
    numericId = 5642
    return numericId


def main():
    # Call functionOne to display the student ID to the console
    functionOne()
    
    # Call functionTwo to prompt for two numbers, print their sum, and store the returned sum
    calculatedSum = functionTwo()
    
    # Call functionThree, passing the calculated sum as an argument, and store the returned numeric student ID
    returnedId = functionThree(calculatedSum)
    
    # Call the print function to output the final message containing the value returned by functionThree
    print(f"functionThree returned the value of {returnedId}")


if __name__ == "__main__":
    main()

