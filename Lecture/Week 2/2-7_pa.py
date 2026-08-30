# Kenneth Irving (kenirv5642)
# Date: 08-30-2026
# Description: Implements a number guessing game and demonstrates the use of 'while' and 'for' loops.

# =============== Inputs ===============
# --- Initial questions ---
studentName = input('Please enter your name: ')
studentID = input('Please enter your Student ID: ')

# =============== Number Guessing Game ===============
# Define variables to track states of the game
targetNum = 5
guessCorrect = False
triesCount = -1 # Will increment to +1 over the first iteration of the loop, so start at -1 to account for that

# Define a function to determine if the guess is correct
def check_guess(guess, targetNum):
    if guess < targetNum:
        return print("You guessed too low")
    elif guess > targetNum:
        return print("You guessed too high")
    else:
        global guessCorrect
        global triesCount
        guessCorrect = True 
        # Since the guess is correct and the loop won't restart to do it, increment the triesCount
        triesCount += 1 
        return print(f'Congratulations! You guessed the number in {triesCount} tries!')
        
while not guessCorrect:
    triesCount += 1
    guess = int(input('Please guess a number between 1 and 10...'))
    check_guess(guess, targetNum)

# =============== Loops ===============
print('\n') # Newline to separate the sections

# Define target number for the loops
targetLoopNum = 5
currentIteration = 0

# --- 'while' loop ---
print("Output from the 'while' loop:")
while (currentIteration < targetLoopNum):
    currentIteration += 1
    outputVar = currentIteration + guess
    print(f'{guess} incremented by {currentIteration} is {outputVar}')

print('\n') # Newline to separate the sections

# --- 'for' loop ---
print("Output from the 'for' loop:")
for currentIteration in range(1, targetLoopNum + 1):
    outputVar = currentIteration + guess
    print(f'{guess} incremented by {currentIteration} is {outputVar}')