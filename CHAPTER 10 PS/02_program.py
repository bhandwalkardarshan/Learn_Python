# Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self, number):
        self.number = number
    def square(self):
        return self.number * self.number
    def cube(self):
        return self.number * self.number * self.number
    def square_root(self):
        return self.number ** 0.5
    
p = Calculator(9)
print(p.square(), p.cube(), p.square_root())