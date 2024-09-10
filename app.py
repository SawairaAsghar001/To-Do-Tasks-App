tasks = []  # Define tasks as a global list

def task():
    global tasks  # Reference the global tasks list
    print("-----WELCOME TO THE TASK MANAGEMENT APP-----")

    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")  # enter task 1 = 
        tasks.append(task_name)
    
    print(f"Today's tasks are\n{tasks}")

# Call the function to execute it
task()

while True:
    operation = int(input("1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\n Enter: "))
    
    if operation == 1:
        add = input("Enter the task you want to add = ")
        tasks.append(add)
        print(f"Task '{add}' has been successfully added...")

    elif operation == 2:
        update_val = input("Enter the task name you want to update = ")
        if update_val in tasks:
            up = input("Enter new task = ")
            ind = tasks.index(update_val)
            tasks[ind] = up
            print(f"Updated task '{up}'")
        else:
            print(f"Task '{update_val}' not found!")

    elif operation == 3:
        del_val = input("Which task do you want to delete = ")
        if del_val in tasks:
            ind = tasks.index(del_val)
            del tasks[ind]
            print(f"Task '{del_val}' has been deleted...")
        else:
            print(f"Task '{del_val}' not found!")

    elif operation == 4:
        print(f"Total tasks = {tasks}")

    elif operation == 5:
        print("Closing the program.....")
        break
    
    else:
        print("Invalid Input. Please select a valid option.")
