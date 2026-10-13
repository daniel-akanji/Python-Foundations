action = input("Hello there!\nSelect an action to proceed:\n1. add tasks\n2. view tasks\n3. remove task\n4. quit:\n")
tasks = []
text = ""
numstr = ""
def pop_up(action):
    action = input("Select an action to proceed:\n1. add tasks\n2. view tasks\n3. remove task\n4. quit:\n")
    print(action)

def add_tasks(text):
    text = input("Specify what task you would like to add: ")
    tasks.append(text)
    pop_up(action)

def view_tasks(tasks):
    for i, task in enumerate(tasks):
        print(f"{task.index[i+1]} {task}")
    pop_up(action)

def remove_tasks(numstr):
    numstr = input("Enter specific task number you wan to remove: ")
    no = int(numstr)
    if (no -1) in range(len(tasks)):
        tasks.pop(no-1)
    else:
        print("Number entered is not in the tasks list")
    pop_up(action)

if action == "1":
    add_tasks(text)
if action == "2":
    view_tasks(tasks)
if action == "3":
    remove_tasks(numstr)
if action == "4":
    print("")
if action not in "1234":
    print("Invalid option number")