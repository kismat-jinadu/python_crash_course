class Employee:
    """display information about employee"""
    def __init__(self,first_name, last_name,annual_salary):
        """define employee info"""
        self.first_name =first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self,increase=5000):
        """give employees of $5000 by default but can be changed"""
        self.annual_salary +=increase
        
