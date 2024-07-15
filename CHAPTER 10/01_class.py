class Employee:
    salary = 120000
    language = "Python"

harry = Employee()
print(harry.salary, harry.language)

darshan = Employee()
print(darshan.language, darshan.salary)

shan = Employee()
shan.name = "Shaan"
print(shan.name, shan.language, shan.salary)

# here name is the instance attribute and salary and languagr attibutes as they directly belongs to class
