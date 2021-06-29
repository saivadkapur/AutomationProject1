#Functions are created mainly for reusability

def printName(name):
    print("My name is " + name)

name1 = input("Please enter your name---> ")
printName(name1)

#RULES TO CREATE A FUNCTION
#def keyword is used to create a function
#function body starts with ():
#first line in the fucntion is always taken as a comment
#return keyword shows end of the function

def hello():
    "First line is always a comment in the function"
    print('hello world')
hello()

#DIFFERENT TYPES OF FUNCTIONS
#Functions not taking any argument and not returning any value
#Function taking agrument but not returning any value
#Functions taking argument and return values as well
#Functions no argument but return value

def sum(a, b):
    print("The sum of two  number = " + str (a+b))

sum(10, 30) #40

def multiple(a,b,c):
    return (a+b)*c

x = multiple(10,2,20)
print(x) #240


def returnData():
    a = 100
    return a

y = returnData()
print(y)
