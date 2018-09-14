

# 1. Create a Class Employee
class Employee:

    e_count = 0
    s_count =0
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        Employee.s_count += salary
        self.department = department
        Employee.e_count +=1
    def get_average(self):
        print(self.s_count/self.e_count)

employee1 = Employee("Soum", "Sean", 5000, "Sale")
employee2 = Employee("Bula", "Math", 5200, "Educ")
employee3 = Employee("Makaba", "Luc", 5000,"Sale")
employee4 = Employee("Kim", "Marc", 5500, "Marketing")
employee5 = Employee("Madoum", "Jean", 6500, "Training")
employee1.get_average()
#b. Create a constructor to initialize name, family, salary, and department

    # def display(self):
    #     print("name:", self.name, "family:", self.family, "salary:", self.salary, "department:", self.department)

#c. create a function to average salary

# class manager(Employee):
#     def __init__(self, name,salary):
#         Employee.__init__(self, name,salary)



        # employee5=manager("Madoum", 6500)
        # employee5.display()

    # def average(salary1, salary, salary3):
    #     return (salary1, salary2, salary3)/3
    #
    # # def average(5000,5200,5000,5500,6500):
    # #   return (5000 + 5200 + 5000 + 5500 + 6500)/5
    #
    #     salary1 = float(input("Please enter salary 1:"))
    #     salary2 = float(input("Please enter salary 2:"))
    #     salary3 = float(input("Please enter salary 3:"))
    #
    #     avg = average(salary1, salary2, salary3)
    #
    #     print('{:.1f}'.format(avg))



    # print("The number of employees is:", Employee.e_count)


    # def __str__(self):
    #     return '{} , id={}, is in {} and is a {}.'.format(self.name, self.family, self.salary, self.department)

#1. Create a data member to count the number of employees

#d Create a Fulltime Employee class that inherits the properties of employee class

class Fulltime_Employee(Employee):
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.department = department

#e. Create the instances of Fulltime Employee class and Employee class and call their member function

class Employee:
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.department = department
class Fulltime_Employee(Employee):
    def __init__(self, name, family, salary, department):
        Employee.init(self, name, family, salary, department)
        self.
