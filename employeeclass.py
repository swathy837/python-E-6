import gc

class Employee:

    # Inner class
    class Address:
        def __init__(self, city, state):
            self.city = city
            self.state = state

        def display_address(self):
            print("City:", self.city)
            print("State:", self.state)

    # Outer class constructor
    def __init__(self, emp_id, name, city, state):
        self.emp_id = emp_id
        self.name = name
        self.address = Employee.Address(city, state)

    # Display employee details
    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        self.address.display_address()


employees = []

while True:
    print("\n1. Hire Employee")
    print("2. Resign Employee")
    print("3. Display Employees")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        city = input("Enter City: ")
        state = input("Enter State: ")

        emp = Employee(emp_id, name, city, state)
        employees.append(emp)
        print("Employee Hired!")

    elif choice == 2:
        emp_id = int(input("Enter ID to remove: "))
        found = False

        for emp in employees:
            if emp.emp_id == emp_id:
                employees.remove(emp)
                found = True
                print("Employee Resigned!")
                break

        if not found:
            print("Employee not found!")

        gc.collect()

    elif choice == 3:
        if len(employees) == 0:
            print("No employees available")
        else:
            for emp in employees:
                print("\n Employee Details :")
                emp.display_employee()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
