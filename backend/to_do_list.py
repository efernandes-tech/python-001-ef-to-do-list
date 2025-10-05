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

if __name__ == "__main__":
    main()
