#take the input from the user and check whether the number is greater than 100 or not

#IF-Else Statements
i = input("Please enter the number -->")
#any value entered by the user in the console will be treated as String by python
#you have to typecast it in the console if you want the value other than string

if(int (i) >100):
    print('The entered number ' + i + ' is greater than 100')
else:
    print('The entered number is less than 100')

#If-Elif-Else Statements & Nested If statements
#1.check if the input number is negative, 2.check if it is zero, 3.if it is greater than 0 check
#whether it is even or odd number

number = input("Enter the number --->")
number = int (number)
if(number <0):
    print("the number is negative")
elif(number > 0):
    print("the number is a postive number")
    if(number % 2 == 0):
        print("the number is even number")
    else:
        print("the number is a odd number")
else:
    print("the number is zero")