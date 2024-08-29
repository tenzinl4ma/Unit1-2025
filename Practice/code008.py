# advance python program to create todo list
# assist from ai assistant
def todo_list():
    tasks = []
    while True:
        action = input("Choose an action: [add/view/rve/quit]: ").strip().lower()
        if action == 'add':
            task = input("Enter a task: ")
            tasks.append(task)
            print("Task added.")
        elif action == 'view':
            print("To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        elif action == 'remove':
            task_num = int(input("Enter task number to remove: ")) - 1
            if 0 <= task_num < len(tasks):
                removed_task = tasks.pop(task_num)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number.")
        elif action == 'quit':
            print("Goodbye!")
            break
        else:
            print("Invalid action.")
todo_list()
