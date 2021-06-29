# logical operators or, and & !

i = input("enter the number -->")
i = int (i)
if(i<0 or i>100):
    print("invalid number")
else:
    print("valid number")

if(i>0 and i%2 == 0):
    print("even number")
else:
    print("odd number")
