class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"Class value of a is {cls.a}")

o = Employee()
o.show()