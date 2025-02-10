def main():
    print("TASK MANAGER")
    print(" [1] Add Task \n [2] View Task \n [3] Mark Task as Complete \n [4] Save Task to a File \n [5] Load Task to a File \n [6] Exit")
    choice = input("Please select an option: ")
    return int(choice)

running = True
while running:
    user_choice = main()
    
    if user_choice == 1:
        pass
    elif user_choice == 2:
        pass
    elif user_choice == 3:
        pass
    elif user_choice == 4:
        pass
    elif user_choice == 5:
        pass
    elif user_choice == 6:
        running = False
    else:
        print("Please select the number that is only provided!")