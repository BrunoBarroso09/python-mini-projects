class ToDo:

    def __init__(self):
        self.task = []
        print("Todo List\n")

    def menu(self):
        while True:
            print("---MENU---\n")
            print("1. Add task")
            print("2. View task")
            print("3. Remove task")
            print("4. Exit\n")

            try:
                menu = int(input("Pick one option: "))
            except ValueError:
                print("Please, insert a valid option!\n")
                continue

            match menu:
                case 1:
                    self.create_task()
                case 2:
                    self.view_task()
                case 3:
                    self.remove_task()
                case 4:
                    print('\nThank you')
                    break
                case _:
                    print("Invalid option")


    def create_task(self):
        new_task = input("Write new task: ")
        self.task.append(new_task)

    def view_task(self):
        return

    def remove_task(self):
        return

task = ToDo()
task.menu()