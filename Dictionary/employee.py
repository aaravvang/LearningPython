"""
Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.

Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"

Use 'assign_department' method to change the department of an employee.
Use 'print_employee_details' method to print the details of an employee.
Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:

overtime = hours_worked - 50
Overtime amount = (overtime * (salary / 50))
"""
class Employee:
  def __init__(self, name, id, salary, dep):
   
    self.emp_name = name
    self.emp_id = id
    self.emp_salary = salary
    self.emp_department = dep
  def assign_department(self, dep):
    self.emp_department = dep
  def print_employee_details(self):
    print("Name:", self.emp_name)
    print("ID:", self.emp_id)
    print("Salary:",self.emp_salary)
    print("Department:", self.emp_department)
  def calc_emp_salary(self, salary, hours_worked):
    salary = self.emp_salary
    if(hours_worked>10):
      overtime = hours_worked - 50
      overtime_amount = (overtime * (salary / 50))
      self.emp_salary+=overtime_amount+(50*50)
    else:
      self.emp_salary = salary+ 50*hours_worked

Aarav = Employee("Aarav",89032,300000,"SALES")
Aarav.assign_department("ACCOUNTING")
Aarav.print_employee_details()
Aarav.calc_emp_salary(Aarav.emp_salary,49)
print(Aarav.emp_salary)
