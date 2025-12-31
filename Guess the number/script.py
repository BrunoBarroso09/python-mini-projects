import random

class Guess:
    def __init__(self):
        self.health = 5
        self.random_number = random.randint(1, 20)
        print(f"Game started and you have {self.health} health.\n")

    def decrease_health(self):
        self.health -= 1
        return self.health

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