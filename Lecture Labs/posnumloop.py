number = int(input("put in a number: "))

while number < 0:
    number = int(input("put in a new number"))

if number > 0:
    print(f"good, a positive, this is your number: {number}")