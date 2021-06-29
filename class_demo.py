#Python is a object oriented programming language
#Class can have variables, functions, constants and constructor
#we can access class memebers by creating an object of the class

#Creating a class
class FirstClass:
    #Creating a Class Function
    def welcome(self): #self key is the default argument when creating a class function
        print("welcome to your first class")

    #Type of Class Functions
    #Function with no argument and no return value
    def hello(self):
        print('hello world')

    #function with arguments and no return value
    def argNoReturn(self, a, b):
        print("sum of two number = " + str(a+b))

    # function with arguments and a return value
    def argReturnValue(self, a, b):
        return a*b

#creating an object of the class 'FirstClass'
fc = FirstClass()

#calling class functions using object 'fc'
fc.welcome() #welcome to your first class
fc.hello() #hello world
fc.argNoReturn(10,20) #sum of two number = 30
x = fc.argReturnValue(2,5)
print(x) #10





