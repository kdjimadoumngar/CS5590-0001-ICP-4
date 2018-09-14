
# Create a function to average salary
nb_salary = int(input("Please enter the  number of salary to be averaged:"))

Salary =[]
for i in range(0,nb_salary):
    salary = int(input("Please enter a salary: "))
    Salary.append(salary)

average=sum(Salary)/nb_salary

print("The average salary is:", round(average,2))
