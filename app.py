import random



def rand0m():
    iter = 0
    while iter < 1:
# Get random number in range 0 through 9.
        r = random.randint(0, 10)
        print(r)
        iter += 1
    

rand0m()

# make user input #

userInput = int(input("Please input your guess from 1-10: "))

if rand0m() == userInput:
        print("You guessed correctly")
elif rand0m() != userInput:
        print("You suck!")


# generate a number int range 1-10
#     print to validate then comment line
#     make into a variable int random #
# DO not print generated number
# Make user input number
#     set as a variable 

# capture the random number from the fuction and set it to a variable to make the answer static and then compare that variable to user input