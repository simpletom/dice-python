from dice.dice import Dice
import getpass


def show_help():
    print("===================================================")
    print("[1]: show help (this text)")
    print("[2]: roll the dice")
    print("[3]: dice options")
    print("[4]: exit the program")
    print("===================================================")


def exit_program():
    global continue_execution
    continue_execution = False
    print("Exiting\n")


def main_loop():
    while True:
        dice = Dice()
        try:
            user_input = int(getpass.getpass("Enter command (1 for help):"))

            if user_input == 1:
                show_help()
            elif user_input == 2:
                dice.roll()
            elif user_input == 3:
                dice.show_help()
                dice.options()
            elif user_input == 4:
                exit("Exiting...")

            else:
                print("Invalid input: " + str(user_input))

        except ValueError:
            print("Input was not a number")


def main():
    print("Welcome to a overblown dice rolling CLI tool\n")
    show_help()
    main_loop()


if __name__ == "__main__":
    main()
