class Company:

    class Employee:
        def __init__(self, emp_id, emp_name, cname):
            self.emp_id = emp_id
            self.emp_name = emp_name
            self.cname = cname

        def display_details(self):
            print("Employee ID:", self.emp_id)
            print("Employee Name:", self.emp_name)
            print("Company Name:", self.cname)
            print()

    def __init__(self, cname):
        self.cname = cname
        self.employees = []

    def add_employee(self, emp_id, emp_name):
        emp = Company.Employee(emp_id, emp_name, self.cname)
        self.employees.append(emp)

    def remove_employee(self, emp_id):
        for e in self.employees:
            if e.emp_id == emp_id:
                self.employees.remove(e)
                print("Employee removed:", emp_id)
                return
        print("Employee not found")

    def display_all(self):
        print("\nEmployee Details:")
        for e in self.employees:
            e.display_details()


cname = input("Enter company name: ")
c = Company(cname)

n = int(input("Enter number of employees: "))

for i in range(n):
    emp_id = int(input("Enter employee id: "))
    emp_name = input("Enter employee name: ")
    c.add_employee(emp_id, emp_name)

c.display_all()

print("Company reference count:", sys.getrefcount(c))

if len(c.employees) > 0:
    print("Employee reference count:", sys.getrefcount(c.employees[0]))

m = int(input("Enter number of employees to remove: "))

for i in range(m):
    rid = int(input("Enter employee id to remove: "))
    c.remove_employee(rid)

c.display_all()

print("Company reference count after removal:", sys.getrefcount(c))

if len(c.employees) > 0:
    print("Employee reference count:", sys.getrefcount(c.employees[0]))

del c

gc.collect()

print("Garbage collection completed")
