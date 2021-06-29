#DIFFERENT TYPES OG ARGUMENTS
#1. Required arguments

def sum(a,b):
    print("sum of the two numbers = " + str (a+b))

#2.Keyword arguments - you sepcify the argument values while calling the function
def sumInput(a,b):
    print("sum of the two numbers = " + str (a+b))

#3.Default arguments - used to fix one or arguments with a default value like b=40 in the below function
#Important thing to remeber using default value as an argument if want to have another argument in the function after
#default value argument that value should also have a default value
#Example: def defaultArg(a=10, b) ***Function throws error since next value after default shouls als have a default value
#Example2: def defArg(a, b=12, c=10) Function gets executed since argument C also has a default value

def sumDefaultArg(a,b=40):
    print("sum of the two numbers = " + str (a+b))


#1
sum(10, 20) #sum of the two numbers = 30
#2
sumInput(b=30, a=20) #sum of the two numbers = 50
#3
sumDefaultArg(15) #sum of the two numbers = 55
sumDefaultArg(25,55) #sum of the two numbers = 80

