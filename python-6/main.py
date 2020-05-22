"""Codenation AceleraDev-Python second challenge.
"""
import abc


class Department:
    """Department representation.
    """
    def __init__(self, name, code):
        """Class initializer.

        Arguments:
            name {str} -- Department name
            code {int} -- Department code
        """
        self.name = name
        self.code = code


class Employee(abc.ABC):
    """The abstract base class Employee doesn't allow direct
    instantiation, so it's necessary to subclass it in order to use its
    resources.
    """
    work_hours = 8

    def __init__(self, code, name, salary):
        """Although it's not possible to instantiate the class, it is
        necessary to initialize it with an initial state.

        Arguments:
            code {int} -- Code number
            name {str} -- Employee name
            salary {float} -- Employee salary
        """
        self.code = code
        self.name = name
        self.salary = salary
        self._department = None

    @abc.abstractmethod
    def calc_bonus(self, percentage):
        """Calculate the employee's bonus.

        Arguments:
            bonus {float} -- Bonus percentage
        """
        pass

    @abc.abstractmethod
    def get_hours(self):
        """Return the employee's working hours.

        Returns:
            int -- Employee working hours
        """
        return Employee.work_hours

    @abc.abstractmethod
    def get_department(self):
        """Return the employee's department name.

        Returns:
            str -- Department name
        """
        return self._department.name

    @abc.abstractmethod
    def set_department(self, name):
        """Change the employee's department name.

        Arguments:
            name {str} -- New department name
        """
        self._department.name = name


class Manager(Employee):
    """Manager is a concrete Employee implementation.
    """
    def __init__(self, code, name, salary):
        """Pass common parameters to is superclass and add it to the
        'managers' department.

        Arguments:
            code {int} -- Code number
            name {str} -- Manager name
            salary {float} -- Manager salary
        """
        super().__init__(code, name, salary)
        self._department = Department('managers', 1)

    def calc_bonus(self, percentage=0.15):
        """Calculate the manager's bonus based on its salary and a
        percentage.

        Keyword Arguments:
            percentage {float} -- Bonus percentage (default: {0.15})

        Returns:
            float -- Bonus value
        """
        return self.salary * percentage

    def get_hours(self):
        """Return the manager's working hours.

        Returns:
            int -- Working hours
        """
        return Manager.work_hours

    def get_department(self):
        """Return the manager's department name.

        Returns:
            str -- Department name
        """
        # As it's not necessary a different behavior we keep the super's
        return super().get_department()

    def set_department(self, name):
        """Change the manager's department name.

        Arguments:
            name {str} -- New department name
        """
        # As it's not necessary a different behavior we keep the super's
        super().set_department(name)


class Seller(Manager):
    """Seller is a concrete Employee implementation.
    """
    def __init__(self, code, name, salary):
        """Pass common parameters to is superclass and add it to the
        'sellers' department.

        Arguments:
            code {int} -- Code number
            name {str} -- Seller name
            salary {float} -- Seller salary
        """
        super().__init__(code, name, salary)
        self._department = Department('sellers', 2)
        self._sales = 0

    def calc_bonus(self, percentage=0.15):
        """Calculate the seller's bonus based on its sales numbers and a
        percentage.

        Keyword Arguments:
            percentage {float} -- Bonus percentage (default: {0.15})

        Returns:
            float -- Bonus value
        """
        return self._sales * percentage

    def get_hours(self):
        """Return the manager's working hours.

        Returns:
            int -- Working hours
        """
        return Seller.work_hours

    def get_department(self):
        """Return the seller's department name.

        Returns:
            str -- Department name
        """
        # As it's not necessary a different behavior we keep the super's
        return super().get_department()

    def set_department(self, name):
        """Change the seller's department name.

        Arguments:
            name {str} -- New department name
        """
        # As it's not necessary a different behavior we keep the super's
        super().set_department(name)

    def get_sales(self):
        """Return the current sales value.

        Returns:
            float -- Total sales
        """
        return self._sales

    def put_sales(self, value):
        """Increase the seller sales.

        Arguments:
            value {flost} -- Value of new sale
        """
        self._sales += value
