
class Departament:
    """Departament representation.
    """
    def __init__(self, name, code):
        """Class initializer.

        Arguments:
            name {str} -- Departament name
            code {int} -- Departament code
        """
        self.name = name
        self.code = code


class Employee():
    """Employee class doesn't allow direct instantiation, it's necessary
    to subclass it in order to use its implementation.
    """
    def __init__(self, code, name, salary):
        """Although it's not possible to instantiate, it's necessary to
        initialize it with an initial state.

        Arguments:
            code {int} -- Code number
            name {str} -- Employee name
            salary {float} -- Employee salary

        Raises:
            TypeError: When trying to instantiate the class
        """
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
        """Return the employee workload hour.

        Returns:
            int -- Employee workload
        """
        return self.hours

    def get_department(self):
        """Return the employee's departament name.

        Returns:
            str -- Departament name
        """
        return self._departament.name

    def set_departament(self, name):
        """Change the employee's departament name.

        Arguments:
            name {str} -- New departament name
        """
        self._departament.name = name


class Manager(Employee):
    """Manager is an Employee.
    """
    def __init__(self, code, name, salary):
        """Pass the common parameters to is superclass and add it to the
        managers departament.

        Arguments:
            code {int} -- Code number
            name {str} -- Manager name
            salary {float} -- Manager salary
        """
        super().__init__(code, name, salary)
        self._departament = Departament('managers', 1)

    def calc_bonus(self, percentage=0.15):
        """Calculate the manager bonus based on the salary and a
        percentage.

        Keyword Arguments:
            percentage {float} -- Bonus percentage (default: {0.15})

        Returns:
            float -- Bonus value
        """
        return self.salary * percentage


class Seller(Employee):
    """Seller is a Employee.
    """
    def __init__(self, code, name, salary):
        """Pass the common parameters to is superclass and add it to the
        sellers departament.

        Arguments:
            code {int} -- Code number
            name {str} -- Seller name
            salary {float} -- Seller salary
        """
        super().__init__(code, name, salary)
        self._departament = Departament('sellers', 2)
        self._sales = 0

    def calc_bonus(self, percentage=0.15):
        """Calculate the seller bonus based on the sales and a
        percentage.

        Keyword Arguments:
            percentage {float} -- Bonus percentage (default: {0.15})

        Returns:
            float -- Bonus value
        """
        return self._sales * percentage

    def get_sales(self):
        """Return the current sales value.

        Returns:
            float -- Total sales
        """
        return self._sales

    def put_sales(self, value):
        """Increase the seller sale.

        Arguments:
            value {flost} -- Value of new sale
        """
        self._sales += value
