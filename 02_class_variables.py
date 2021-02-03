class Employee:

    # class variables
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay 
        self.email = first + "." + last + "@company.com"
        
        Employee.num_of_emps += 1 #Increase num of emps with each new employee

    def fullname(self):
        return f"{self.first}, {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("Kay", "Kozaronek", 50000)
emp_2 = Employee("Julita", "Swiatek", 60000)

emp_1.raise_amount = 1.05 

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

print(Employee.num_of_emps)


# Inheritance of class variable - raise_amount 

# print(emp_1.__dict__) # prints namespace - there's no raise amount there
# print(Employee.__dict__) # prints namespace of Employee class

# print("raise_amount" in emp_1.__dict__)
# print("raise_amount" in Employee.__dict__)