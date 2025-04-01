import random
#import a group of random methods

number = random.randint(0, 100)
#pulls a random number and assigns it to the number variable

print("Guess a number between 0 and 100")

guess = -1


while guess != number:
    guess = int(input("\nEnter your guess:"))
#commands user input to assign it to their guess variable

    if guess == number:
        print(f"Yes, the number is {number}")
    elif guess > number:
        print("Your guess is too high")
    elif guess < number:
        print("Your number is too low")
#lets you know if your number is too high, too low or is the correct answer