"""Create a class named Employee with properties name, age, and salary. Add a method give_raise() that increases the employee's salary by 10%."""



class Employee:
  age = 0
  name = "John"
  salary = 5000
  def give_raise(self):
    self.salary*=1.1
  def printSalary(self):
    print(self.salary)

  @staticmethod
  def work():
    print("i am working")


John = Employee() #creating an object
John.give_raise()
John.printSalary()

Rohan = Employee() #creating an object
Rohan.give_raise()
Rohan.printSalary()

Aarav = Employee() #creating an object
Aarav.give_raise()
Aarav.printSalary()

Employee.work() #calling the static method


