userinput = input("do you want to continue this loop y/n: ")
count = 0

while userinput == "y":
    userinput = input("do you want to continue this loop y/n: ")
    count += 1
    
if userinput == "n":
    print(f"the loop happened {count} times")