tasks = []

while True:
    action = input("Menu: add | view | remove | done | quit\n")

    def add_tasks():
        task = input("> ")
        tasks.append([[], task])
        print("Task added.")

    def view_task():
        for i, task in enumerate(tasks):
            print(f'{i+1} {task[0]} {task[1]}')

    def remove_task():
        element = input("Enter task number to remove: ")
        no = int(element)
        tasks.pop(no-1)
        print("Task removed.")

    def done_task():
        num = input(">done ")
        number = int(num)
        for i, task in enumerate(tasks):
            if number == i+1:
                task[0].append("x")
        print(f"Task {number} marked as done.")


    if action == 'add':
        add_tasks()
    elif action == 'view':
        view_task()
    elif action == 'remove':
        remove_task()
    elif action == 'done':
        done_task()
    elif action == 'quit':
        print('Goodbye')
        break