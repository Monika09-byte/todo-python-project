tasks  = []
while True:
    print("\n----TO-DO LIST ----")
    print("1.Add Task")
    print("2.View Task")
    print("3.Delete Task")
    print("4.Exit")

    choice = input("Enter your choice: ")

    if choice == "3":
        print("Goodbye!")
        break
    elif choice =="1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully")
    elif choice =="2":
        if not tasks:
            print("No tasks available")
        else:
            for i,task in enumerate(tasks,start=1):
                print(i,task)
  