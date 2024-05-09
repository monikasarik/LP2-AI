class Employee:
    def __init__(self, name):
        self.name = name
        self.scores = {}

    def add_score(self, criteria, score):
        self.scores[criteria] = score

    def get_score(self, criteria):
        return self.scores.get(criteria)

class PerformanceEvaluationSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, name):
        employee = Employee(name)
        self.employees[name] = employee
        print(f"Employee {name} added successfully.")

    def evaluate_employee(self, name):
        employee = self.employees.get(name)
        if not employee:
            print("Employee not found.")
            return
        print(f"Performance Evaluation for Employee {name}:")
        for criteria, score in employee.scores.items():
            print(f"{criteria}: {score}")

    def add_score(self, name, criteria, score):
        employee = self.employees.get(name)
        if not employee:
            print("Employee not found.")
            return
        employee.add_score(criteria, score)
        print(f"Score added successfully for Employee {name}.")

# Example usage
performance_system = PerformanceEvaluationSystem()

while True:
    print("\nEmployee Performance Evaluation System")
    print("1. Add Employee")
    print("2. Evaluate Employee")
    print("3. Add Score")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter employee name: ")
        performance_system.add_employee(name)
    elif choice == '2':
        name = input("Enter employee name: ")
        performance_system.evaluate_employee(name)
    elif choice == '3':
        name = input("Enter employee name: ")
        criteria = input("Enter evaluation criteria: ")
        score = input("Enter score: ")
        performance_system.add_score(name, criteria, score)
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")