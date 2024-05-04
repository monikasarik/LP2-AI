#Information Management System
class InformationManagementSystem:
    def __init__(self):
        self.information = {}

    def add_information(self, key, value):
        self.information[key] = value
        print("Information added successfully!")

    def get_information(self, key):
        if key in self.information:
            print(f"{key}: {self.information[key]}")
        else:
            print("Information not found.")

    def update_information(self, key, value):
        if key in self.information:
            self.information[key] = value
            print("Information updated successfully!")
        else:
            print("Information not found.")

    def delete_information(self, key):
        if key in self.information:
            del self.information[key]
            print("Information deleted successfully!")
        else:
            print("Information not found.")

# Example usage with user input:
info_system = InformationManagementSystem()

while True:
    print("\n1. Add Information\n2. Get Information\n3. Update Information\n4. Delete Information\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        key = input("Enter key: ")
        value = input("Enter value: ")
        info_system.add_information(key, value)
    elif choice == '2':
        key = input("Enter key: ")
        info_system.get_information(key)
    elif choice == '3':
        key = input("Enter key: ")
        value = input("Enter new value: ")
        info_system.update_information(key, value)
    elif choice == '4':
        key = input("Enter key: ")
        info_system.delete_information(key)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
