# Python Object-Oriented Programming

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee("Gerold", "Csendes", 50000)
emp_2 = Employee("Kay", "Kozaronek", 0)

print(emp_1.first)
print(emp_2.email)

emp_2.fullname()