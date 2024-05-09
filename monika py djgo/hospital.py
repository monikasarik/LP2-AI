#Hospital & Medical Facility Management
class HospitalManagementSystem:
    def __init__(self):
        self.patients = {}

    def admit_patient(self, patient_id, name, condition):
        self.patients[patient_id] = {'name': name, 'condition': condition}
        print("Patient admitted successfully!")

    def discharge_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]
            print("Patient discharged successfully!")
        else:
            print("Patient not found.")

    def update_patient_condition(self, patient_id, condition):
        if patient_id in self.patients:
            self.patients[patient_id]['condition'] = condition
            print("Patient condition updated successfully!")
        else:
            print("Patient not found.")

    def get_patient_info(self, patient_id):
        if patient_id in self.patients:
            print(f"Patient ID: {patient_id}")
            for key, value in self.patients[patient_id].items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("Patient not found.")

# Example usage with user input:
hospital_system = HospitalManagementSystem()

while True:
    print("\n1. Admit Patient\n2. Discharge Patient\n3. Update Patient Condition\n4. Get Patient Information\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        patient_id = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        condition = input("Enter patient condition: ")
        hospital_system.admit_patient(patient_id, name, condition)
    elif choice == '2':
        patient_id = input("Enter patient ID: ")
        hospital_system.discharge_patient(patient_id)
    elif choice == '3':
        patient_id = input("Enter patient ID: ")
        condition = input("Enter new condition: ")
        hospital_system.update_patient_condition(patient_id, condition)
    elif choice == '4':
        patient_id = input("Enter patient ID: ")
        hospital_system.get_patient_info(patient_id)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")