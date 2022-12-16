class Employee:
    __slots__ = ('first', 'last')

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, fullname):
        self.first = fullname.split(" ")[0]
        self.first = fullname.split(" ")[0]

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

if __name__ == "__main__":
    emp_1 = Employee('John', 'Smith')

    print(emp_1.first)
    print(emp_1.email)
    print(emp_1.fullname)

    emp_1.fullname = "Corey Schafer"
    print(emp_1.first)
    print(emp_1.email)
    print(emp_1.fullname)

    del emp_1.fullname
    print(emp_1.first)
    print(emp_1.email)
    print(emp_1.fullname)