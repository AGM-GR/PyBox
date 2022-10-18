import random


// Guess a number between 1 and 50
def magic_number():
    number = random.randint(1,50)
    guess = 0

    while guess != number:
        guess = int(input("Give me a number: "))

        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print("Congratulations, you got it!")

magic_number()
