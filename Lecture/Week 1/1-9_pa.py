# kenirv5642

# ===== Inputs =====
# --- Initial questions ---
studentName = input('Please enter your name: ')
studentID = input('Please enter your Student ID: ')

# --- Ask for whole numbers ---
num1 = int(input('Please enter a whole number: '))
num2 = int(input('Please enter a different second whole number: '))

# --- Math calculations ---
res1 = float(num1 * num2)   # Multiplication
res2 = float(num1 / num2)   # Division
res3 = float(num1 + num2)   # Addition

# ===== Outputs =====
print('\n') # Newline to separate the sections

# --- Math calculation's results ---
print(f'The result of {num1} times {num2} is: ${res1:,.2f}')
print(f'The result of {num1} divided by {num2} is: ${res2:,.2f}')
print(f'The result of {num1} plus {num2} is: ${res3:,.2f}')

# --- Compare the numbers ---
if (num1 > num2):
    print(f'Number 1 ({num1}) is larger than Number 2 ({num2})')
elif (num1 < num2):
    print(f'Number 2 ({num2}) is larger than Number 1 ({num1})')
else:
    print(f'Number 1 ({num1}) and Number 2 ({num2}) are the same.')

# --- Initial questions ---
print(f'{studentName}')
print(f'{studentID}')