

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee():
    def __init__(self, code, name, salary):
        if type(self) == Employee:
            raise TypeError("Direct instantiation is not allowed.")
        self.code = code
        self.name = name
        self.salary = salary
        self.hours = 8
        self._departament = None

    def calc_bonus(self, percentage):
        raise NotImplementedError("Mandatory subclass implementation")

    def get_hours(self):
        raise NotImplementedError("Mandatory subclass implementation")

    def get_departament(self):
        raise NotImplementedError("Mandatory subclass implementation")

    def set_department(self, name):
        raise NotImplementedError("Mandatory subclass implementation")


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('managers', 1)

    def calc_bonus(self, percentage=0.15):
        return self.salary * percentage

    def get_hours(self):
        return self.hours

    def get_departament(self):
        return self._departament.name

    def set_department(self, name):
        self._departament.name = name


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('sellers', 2)
        self._sales = 0

    def calc_bonus(self, percentage=0.15):
        return self._sales * percentage

    def get_hours(self):
        return self.hours

    def get_sales(self):
        return self._sales

    def put_sales(self, value):
        self._sales += value

    def get_departament(self):
        return self._departament.name

    def set_department(self, name):
        self._departament.name = name
