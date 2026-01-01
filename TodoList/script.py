class ToDo:

    def __init__(self):
        self.tasks = []
        print("Todo List\n")

    def menu(self):
        while True:
            print("\n---MENU---\n")
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
        self.tasks.append(new_task)

    def view_task(self):
        if not self.tasks:
            print("Empty list")
        else:
            print("Todo List\n")
            for task in self.tasks:
                print(f"{task:^15}")

    def remove_task(self):
        if not self.tasks:
            print("empty")
            return
        try:
            for i, task in enumerate(self.tasks):
                print(f"Position: {i + 1} - task: {task}")
            remove = int(input("Pick the position to remove: "))
            self.tasks.pop(remove - 1)
            print("✅ Task removed successfully!")
        except ValueError:
            print('\n🚨 Error: Please insert a valid NUMBER (e.g., 1, 2, 3).')
        except IndexError:
            print('\n🚨 Error: Task you are trying to remove is not in the list.')

task = ToDo()
task.menu()