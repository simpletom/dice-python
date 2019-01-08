import random
import getpass

min_value = 1
max_value = 6
history = []


def options():
    show_options = True
    while show_options:
        try:
            user_input = int(getpass.getpass("Dice options (1 for help)"))

            if user_input == 1:
                show_help()
            elif user_input == 2:
                show_history()
            elif user_input == 3:
                clear_history()
            elif user_input == 4:
                show_last_roll()
            elif user_input == 5:
                show_average_roll()
            elif user_input == 6:
                details()
            elif user_input == 7:
                modify()
            elif user_input == 8:
                show_options = False
            else:
                print("Invalid input: " + str(user_input))

        except ValueError:
            print("Invalid input: " + str(user_input))


def show_help():
    print("===================================================")
    print("[1]: show help (this text)")
    print("[2]: show history")
    print("[3]: clear history")
    print("[4]: show last roll")
    print("[5]: show average roll")
    print("[6]: show type of dice")
    print("[7]: set the number of faces")
    print("[8]: exit this menu")
    print("===================================================")


def details():
    print("Dice is a 1d" + str(max_value))


def show_history():
    print("Previous rolls: " + str(history))


def clear_history():
    global history
    history = []
    print("History cleared")


def modify():
        try:
            user_input = getpass.getpass("Number of faces?")
            faces = int(user_input)
            global max_value
            max_value = faces
            print("Dice is now a 1d" + str(max_value) + " dice\n")
        except ValueError:
            print("Invalid input: " + str(user_input) + "\n")


def roll():
    print("Rolling...")
    current_roll = random.randint(min_value, max_value)
    print("=> " + str(current_roll) + "\n")
    history.append(current_roll)


def show_average_roll():
    average = 0
    rolls = len(history)

    if rolls != 0:
        average = sum(history) / rolls

    print("Average of " + str(rolls) + " rolls: " + str(average) + "\n")


def last_roll():
    global history
    try:
        return history[-1]
    except IndexError:
        return 0


def show_last_roll():
    print(last_roll())
