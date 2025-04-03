print("Welcome to the most simple password generator!")
numpass = int(input("\nEnter number of passwords:"))
numlength = int(input("\nEnter length of passwords:"))

print("\nHere are your passwords:")

import random
import string

characters = string.digits + string.ascii_letters + string.punctuation

for i in range(numpass):
        print (''.join(random.choice(characters) for i in range(numlength)))