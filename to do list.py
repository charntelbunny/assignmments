tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

    elif choice == "3":
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)

    elif choice == "4":
        print("Goodbye!")
        break