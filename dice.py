import random
min_value = 1
max_value = 6

continue_execution = True
roll_history = []


def show_help():
    print()
    print("=== HELP ===")
    print("help: this output")
    print("roll: rolls the dice and appends result to history")
    print("history: prints the previous rolls")
    print("clear: clears the history of previous rolls")
    print("dice: set the number of faces for the dice, must be a number")
    print("exit: exits the program\n")


def print_history():
    print("Previous rolls:\n")
    print(roll_history)


def clear_history():
    global roll_history
    roll_history = []
    print("History cleared\n")


def roll_the_dice():
    print("Rolling dice...")
    roll = random.randint(min_value, max_value)
    print("You got a: " + str(roll) + "\n")
    roll_history.append(roll)
    roll_again()


def exit_program():
    global continue_execution
    continue_execution = False
    print("Exiting\n")


def set_dice():
    user_input = input("How many faces should the dice have?\n")
    try:
        faces = int(user_input)
        global max_value
        max_value = faces
        print("Dice is now a 1d" + str(max_value) + " dice\n")
    except ValueError:
        print("Input was not a number\n")


def roll_again():
    reroll = input("Roll again?\n")
    if reroll == "y" or reroll == "yes":
        roll_the_dice()
    elif reroll == "n" or reroll == "no":
        pass
    else:
        print("Valid inputs are \"yes\", \"y\", \"no\", \"n\"")
        roll_again()


while continue_execution:
    key_input = input("Please enter command (\"help\" for help)\n")

    if key_input == "exit":
        exit_program()
    elif key_input == "history":
        print_history()
    elif key_input == "roll":
        roll_the_dice()
    elif key_input == "dice":
        set_dice()
    elif key_input == "help":
        show_help()
    else:
        print("Wrong command, please enter again")
