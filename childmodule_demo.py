import module_demo

#once the import is imported then the executable code will automatically execute
#welcome to to python module - module_demo.py

#below is the code to execute module function
module_demo.hello() #printing module function without a class
x = module_demo.sum(2,3)
print(x) #5

#below code to execute class functions of a module
obj = module_demo.Plane()
#OUTPUT:
#Accelerating
#Changing flaps
#Closing wheels