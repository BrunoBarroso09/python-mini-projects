class Calculator():

    def __init__(self):
        print("Calculator\n")

    def menu(self):
        while True:
            print("--- MENU ---")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")

            try:
                option = int(input("Pick one option: "))

                match option:
                    case 1:
                        self.add()
                    case 2:
                        self.subtract()
                    case 3:
                        self.multiply()
                    case 4:
                        self.divide()
                    case 5:
                        print('\nThank you')
                        break
                    case _:
                        print("Invalid option")
            except ValueError:
                print("Please, insert a valid option!\n")
                continue

    def get_numbers(self):
        first_operator = int(input("Write first operator: "))
        second_operator = int(input("Write second operator: "))
        return first_operator, second_operator

    def add(self):
        try:
            n1, n2 = self.get_numbers()
            result = n1 + n2
            print(f"Result: {result}\n")
        except ValueError:
            print("Please, insert a valid value!\n")

    def subtract(self):
        try:
            n1, n2 = self.get_numbers()
            result = n1 - n2
            print(f"Result: {result}\n")
        except ValueError:
            print("Please, insert a valid value!\n")

    def multiply(self):
        try:
            n1, n2 = self.get_numbers()
            result = n1 * n2
            print(f"Result: {result}\n")
        except ValueError:
            print("Please, insert a valid value!\n")

    def divide(self):
        try:
            n1, n2 = self.get_numbers()
            result = n1 / n2
            print(f"Result: {result}\n")
        except ZeroDivisionError:
            print("Division by zero is not allowed!\n")
        except ValueError:
            print("Please, insert a valid value!\n")

calc = Calculator()
calc.menu()