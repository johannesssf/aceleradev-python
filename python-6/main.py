import abc


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(abc.ABC):
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary
        self.hours = 8
        self.__departament = None

    @abc.abstractmethod
    def calc_bonus(self, bonus):
        pass

    @abc.abstractmethod
    def get_hours(self):
        pass

    @abc.abstractmethod
    def get_departament(self):
        pass

    @abc.abstractmethod
    def set_department(self, department):
        pass


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.set_department(Department('managers', 1))

    def calc_bonus(self, bonus=0.15):
        return self.salary * bonus

    def get_hours(self):
        return self.hours

    def get_departament(self):
        return self.__departament.name

    def set_department(self, department):
        self.__departament = department


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.set_department(Department('sellers', 2))
        self.__sales = 0

    def calc_bonus(self, bonus=0.15):
        return self.__sales * bonus

    def get_hours(self):
        return self.hours

    def get_sales(self):
        return self.__sales

    def put_sales(self, value):
        self.__sales += value

    def get_departament(self):
        return self.__departament.name

    def set_department(self, department):
        self.__departament = department


if __name__ == "__main__":
    # employee = Employee(1, 2, 2)
    manager = Manager(1, 'Johannes', 1000)
    print(manager.get_departament())
