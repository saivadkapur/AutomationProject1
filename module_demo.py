#Module can be defined as Python files with .py extension, modules can have executable code,module functions and classes
#classes can also have functions, constructors, variables

#Direct Executable code
print("welcome to to python module - module_demo.py")

#Module Function without a class
def hello():
    print('printing module function without a class')

def sum(a, b):
    return a+b

#Module Class and class function
class Plane:
    def __init__(self):
        self.wings = 2

        # fly
        self.drive()
        self.flaps()
        self.wheels()

    def drive(self):
            print('Accelerating')

    def flaps(self):
            print('Changing flaps')

    def wheels(self):
            print('Closing wheels')

#ba = Plane()
#hello()