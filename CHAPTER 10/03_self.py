class Employee:
    salary = 120000
    language = "Python"

    def getInfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning, Sir")

harry = Employee()
# print(harry.salary, harry.language)
harry.language = "JS"

harry.getInfo()
Employee.getInfo(harry)