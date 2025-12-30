import random

class Guess:
    def __init__(self):
        self.health = 5
        self.random_number = random.randint(1, 20)
        print(f"Game started and you have {self.health} health.\n")

    def decrease_health(self):
        pass

    def play(self):
        while self.health > 0:
            pass
        print("Game Over! The guess number is", self.random_number)

game = Guess()
game.play()