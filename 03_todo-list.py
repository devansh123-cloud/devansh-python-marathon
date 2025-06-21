task = {}

while True:
    print("\n--- TodoList---")
    print("1. Enter Task")
    print("2. Edit Task")
    print("3. View All Tasks")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_task = (str)(input("Enter new task: "))
        add_date = (input("Enter date to complete the task: "))
        add_time = (input("Enter time to complete the task: "))
        add_day =   (str)(input("Enter day to complete the task: "))

        task[add_day] = {
            "add_task": add_task,
            "add_date": add_date,
            "add_time": add_time
        }
        print("✅ Task added!")
        
    elif choice == "2":
        edit_day = input("Enter Day to Edit Task:")
        
