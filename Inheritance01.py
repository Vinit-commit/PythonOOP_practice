class Employee:
    def __init__(self, name, employee_id):
        self.name = name 
        self.employee_id = employee_id

    def show_details(self):
        return f"ID: {self.employee_id}, Name: {self.name}"
    

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def show_details(self):
        base_details = super().show_details()
        return f"{base_details}, Department: {self.department}"
    

emp = Employee("Arjun Sharma", "E123")
mgr = Manager("Priya Singh", "M456", "Technology")


print(emp.show_details())

print(mgr.show_details())