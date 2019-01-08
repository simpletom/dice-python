import random
import getpass


class Dice:

    def __init__(self):
        self.min_value = 1
        self.max_value = 6
        self.history = []

    def options(self):
        show_options = True
        while show_options:
            try:
                user_input = int(getpass.getpass("Dice options (1 for help)"))

                if user_input == 1:
                    self.show_help()
                elif user_input == 2:
                    self.show_history()
                elif user_input == 3:
                    self.clear_history()
                elif user_input == 4:
                    self.show_last_roll()
                elif user_input == 5:
                    self.show_average_roll()
                elif user_input == 6:
                    self.details()
                elif user_input == 7:
                    self.modify()
                elif user_input == 8:
                    show_options = False
                else:
                    print("Invalid input: " + str(user_input))

            except ValueError:
                print("Invalid input: " + str(user_input))


    def show_help(self):
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


    def details(self):
        print("Dice is a 1d" + str(self.max_value))


    def show_history(self):
        print("Previous rolls: " + str(self.history))


    def clear_history(self):
        self.history = []
        print("History cleared")


    def modify(self):
            try:
                user_input = getpass.getpass("Number of faces?")
                faces = int(user_input)
                self.max_value = faces
                print("Dice is now a 1d" + str(self.max_value) + " dice\n")
            except ValueError:
                print("Invalid input: " + str(user_input) + "\n")


    def roll(self):
        print("Rolling...")
        current_roll = random.randint(self.min_value, self.max_value)
        print("=> " + str(current_roll) + "\n")
        self.history.append(current_roll)
        return current_roll


    def show_average_roll(self):
        rolls = len(self.history)

        print("Average of " + str(rolls) + " rolls: " + str(self.average_roll) + "\n")


    def last_roll(self):
        try:
            return self.history[-1]
        except IndexError:
            return 0

    def average_roll(self):
        average = 0
        rolls = len(self.history)

        if rolls != 0:
            average = sum(self.history) / rolls

        return average

    def show_last_roll(self):
        print(self.last_roll() +"\n")
