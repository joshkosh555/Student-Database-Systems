class mainmenuC:
    def __init__(self, studentlist, registration, search, print_student):
        self.studentlist = studentlist
        self.registration = registration
        self.search = search
        self.print_student = print_student

    def mainm(self, menu, user):
        while True:
            print(f"\n\nWelcome, Admin {user.get_name()}!")
            print("Please choose from the following options:")
            print("\n====================== Student Database Menu =====================")
            print("1. View your information")
            print("2. View other student's information")
            print("3. Register a New Student")
            print("4. Print all students in the list")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                print(f"\n{user}")

            elif choice == '2':
                id_number = input("Enter the Student ID to search: ")
                student = next((i for i in menu if i.get_id_number() == id_number), None)
                if student:
                    print(f"\n{student}")
                else:
                    print("\nStudent not found.")

            elif choice == '3':
                self.registration.add_student()
                onemore = input("Do you want to add another student? (Y/N): ").lower()
                if onemore != 'y':
                    continue

            elif choice == '4':
                self.print_student.print_allstudents(menu)

            elif choice == '5':
                print("Exiting program...")
                exit()

            else:
                print("Invalid choice. Please try again.")
