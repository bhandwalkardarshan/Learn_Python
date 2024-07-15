class Employee:
    salary = 120000
    language = "Python"

    def __init__(self, name, salary, language):             # dunder method which calls automatically
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning, Sir")

harry = Employee("Harry", 1900000, "Javascript")
print(harry.name, harry.language, harry.salary)