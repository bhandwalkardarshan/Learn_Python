class Employee:
    company = "ITC"
    def show(self):
        print(f"My name is {self.name} and my salary is {self.salary}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"My name is {self.name} and my salary is {self.salary}")
    
    # def showLanguage(self):
    #     print(f" My name is {self.name} and I am working on {self.language}")
    
class Programmer(Employee):
    def showLanguage(self):
        print(f"My name is {self.name} and I am working on {self.language}")

a = Employee()
b = Programmer()

print(a.company, b.company)