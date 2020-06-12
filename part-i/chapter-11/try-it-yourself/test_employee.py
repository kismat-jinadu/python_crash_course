import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Set up employee info and salary"""
        self.employee = Employee('Jay','Zee',100000)
    
    def test_give_default_raise(self):
        """to test that you can give default raise"""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary,105000)


    def test_give_custom_raise(self):
        """to test that you can give any amount of raise"""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary,110000)

if __name__ =='__main__':
    unittest.main()