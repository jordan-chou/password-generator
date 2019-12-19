#   Jordan Chou
#   Dec. 18, 2019
#   A password generator

import random
import string
password = ""

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not an integer! Try again\n")
            continue
        else:
            return userInput
            break

print("Password Generator\n")

while True:
    passLength = inputNumber("How long do you want your password to be? ")
    if passLength < 6:
        print("Must be at least 6 characters long. Try again\n")
    else:
        break

while True:
    maxLetters = inputNumber("How many letters do you want in your password? ")
    if maxLetters <= 0:
        print("There must be at least 1 letter. Try again\n")
    elif maxLetters > passLength:
        print("That is too many letters. Try again\n")
    else:
        break

if (passLength - maxLetters) > 0:
    while True:
        maxNumbers = inputNumber("How many numbers do you want in your password?\nThe rest will be symbols: ")
        if maxNumbers < 0:
            print("There cannot be negative numbers. Try again\n")
        elif maxNumbers > (passLength - maxLetters):
            print("That is too many numbers. Try again\n")
        else:
            break

maxSymbols = passLength - maxLetters - maxNumbers


# Generate random ASCII values for numbers and letters
numOfLetters, numOfNumbers, numOfSymbols = 0, 0, 0
print()

# Generate the random letters you need
while numOfLetters < maxLetters:
    password += random.choice(string.ascii_letters)
    numOfLetters += 1
    print("Generating letter: " + password)

print()
# Generate the random numbers
while numOfNumbers < maxNumbers:
    password += random.choice(string.digits)
    numOfNumbers += 1
    print("Generating number: " + password)

if maxSymbols > 0:
    print()
# Generate the remaining random symbols
while numOfSymbols < maxSymbols:
    password += random.choice(string.punctuation)
    numOfSymbols += 1
    print("Generating symbol: " + password)

# Shuffle the password
pwList = list(password)
random.shuffle(pwList)
password = "".join(pwList)
print("\nShuffing...")

print("\nYour generated password is " + password)
