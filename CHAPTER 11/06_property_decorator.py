class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"Class value of a is {cls.a}")
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname, self.lname = value.split(" ")

o = Employee()
o.a = 45

o.name = "Siya Rajput"
print(o.fname, o.lname)

o.show() 