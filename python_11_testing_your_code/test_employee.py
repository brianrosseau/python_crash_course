# first we write the tests without a fixture...
from employee import Employee

def test_give_default_raise():
    """Test that default raise is given properly."""
    brian = Employee('brian', 'rosseau', 50000)
    brian.get_raise()
    assert brian.salary == 55000

def test_give_custom_raise():
    """Test that custom raise if given properly."""
    brian = Employee('brian', 'rosseau', 50000)
    brian.get_raise(10000)
    assert brian.salary == 60000

# both tests above pass!


# Next, we re-write the test with a fixture so we don't have to create a new
#   employee instance with each test function.
import pytest
from employee import Employee

@pytest.fixture
def fixture_employee():
    """Make a fixture employee to use in all test functions."""
    fixture_employee = Employee('brian', 'rosseau', 50000)
    return fixture_employee

def test_give_default_raise(fixture_employee):
    """Test that default raise is given properly."""
    fixture_employee.get_raise()
    assert fixture_employee.salary == 55000

def test_give_custom_raise(fixture_employee):
    """Test that custom raise is given properly."""
    fixture_employee.get_raise(10000)
    assert fixture_employee.salary == 60000

# this passes as well!