def main():
    while True:
        print("\nTask Manager")
        print("1. Say Hello")
        print("2. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Hello, welcome to the CLI app!")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

