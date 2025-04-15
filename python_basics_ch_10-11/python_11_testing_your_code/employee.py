class Employee:
    """A class to represent an employee."""

    def __init__(self, first, last, salary):
        """Initialize the employee."""
        self.first_name = first.title()
        self.last_name = last.title()
        self.salary = salary

    def get_raise(self, amount=5000):
        """Give the employee a raise to annual salary: $5000 by default, but also accepts different raise amounts."""
        self.salary += amount
    