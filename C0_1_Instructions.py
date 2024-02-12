print("🎲🎲 Roll it 13 🎲🎲")


# loop for testing purposes

while True:
    want_instruction = input("Do you want to read the instructions? ") .lower()

    # checks users enter yes (y) or no (n)
    if want_instruction == "yes"  or want_instruction == "y" :
        print("you chose yes")
    elif want_instruction == "no"  or want_instruction == "n":
        print ("you chose no")
    else:
        print("You did not choose a valid response")