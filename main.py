class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the TODO list.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed from the TODO list.')
        else:
            print(f'Task "{task}" not found in the TODO list.')

    def display_tasks(self):
        if not self.tasks:
            print('TODO list is empty.')
        else:
            print('TODO list:')
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. {task}')

def main():
    todo_list = TodoList()

    while True:
        print('\nTODO List Menu:')
        print('1. Add Task')
        print('2. Remove Task')
        print('3. Display Tasks')
        print('4. Quit')

        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            task = input('Enter the task to remove: ')
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print('Exiting the TODO list program. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 4.')

if __name__ == "__main__":
    main()
