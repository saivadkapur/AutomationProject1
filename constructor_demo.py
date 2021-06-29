#Constructor is a special type of method
#created with __init()__, first argument is always self
#automatically called when object is created
#can take arguments
#constructor never return any value
#constructor are used for initialization

class ConstructorDemo:
    "Creating a constructor"
    def __init__(self, a, b):
        print(a+b)
       #return a+b this return statement will throw an error since constructor can't return a value

    #general function
    def hello(self):
        print('hello world')

#Creating an object to the class and calling the constructor at the same type
#below line of code will automatically calls the constructor function

#cd = ConstructorDemo(10, 20) #30
#cd.hello() #hello world