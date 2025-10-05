def show_menu():
    print("\n=== To Do List ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Exit")

def main():
    tasks = []

    while True:
        show_menu()
        choice = input("\nChoose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
        return

    print("\nYour tasks:")
    for i, task in enumerate(tasks, 1):
        status = "x" if task["completed"] else "-"
        print(f"{i}. [{status}] {task['description']}")

def add_task(tasks):
    description = input("\nEnter task description: ")
    task = {
        "description": description,
        "completed": False
    }
    tasks.append(task)
    print(f"Added: {description}")

def complete_task(tasks):
    if not tasks:
        print("\nNo tasks to complete!")
        return

    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("Task completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
