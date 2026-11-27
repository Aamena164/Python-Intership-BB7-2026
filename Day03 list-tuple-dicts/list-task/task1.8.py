tasks=[]

while True:
    print("1. Add a task")
    print("2. View all tasks")  
    print("3. Delete a task")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")
    elif choice == '2':
        if tasks:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i,". ", task)
        else:
            print("No tasks available.")
    elif choice == '3':
        if tasks:
            task = input("Enter the task number to delete: ")
            try:
                task = int(task)
                if 1 <= task <= len(tasks):
                    tasks.pop(task - 1)
                    print("Task deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid task number.")
        else:
            print("No tasks available.")
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")