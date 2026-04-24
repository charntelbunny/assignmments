students = []
scores = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Show Average")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter student name: ")
        score = int(input("Enter score: "))
        students.append(name)
        scores.append(score)

    elif choice == "2":
        print("\nStudent Scores:")
        for i in range(len(students)):
            print(students[i], ":", scores[i])

    elif choice == "3":
        if len(scores) > 0:
            avg = sum(scores) / len(scores)
            print("Average score:", avg)
        else:
            print("No data")

    elif choice == "4":
        print("Goodbye!")
        break