import random

class Guess:
    def __init__(self):
        self.health = 0
        self.random_number = random.randint(1, 20)
        print(f"Game started.\n")
        self.menu()

    def decrease_health(self):
        self.health -= 1
        return self.health

    def menu(self):
        print("---Difficulty---\n")
        print("1. Easy\n")
        print("2. Medium\n")
        print("3. Hard\n")
        try:
            difficulty = int(input("Select the difficulty: "))
            match difficulty:
                case 1:
                    print("Selected the easy mode")
                    self.health = 7
                case 2:
                    print("Selected the medium mode")
                    self.health = 5
                case 3:
                    print("Selected the hard mode")
                    self.health = 3
                case _:
                    print("Invalid option")
        except ValueError:
            print("Please, insert a valid option!")

    def play(self):
        while self.health > 0:
            try:
                user_number = int(input("Write a number between 1 to 20: "))
                if user_number == self.random_number:
                    print("\n🎉 Congrats! You guess the number.")
                    return
                elif user_number <= 0:
                    print("The number need to be higher than 0.\n")
                elif user_number > self.random_number:
                    print(f"\nYour number is higher than the guess number and you lost 1 health. You have {self.decrease_health()} health.\n")
                else:
                    print(f"\nYour number is less than the guess number and you lost 1 health. You have {self.decrease_health()} health.\n")
            except:
                print("An exception occurred")
        print("Game Over! The guess number was", self.random_number)

game = Guess()
game.play()