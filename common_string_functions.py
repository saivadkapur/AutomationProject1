#String Functions
stringEmail = 'www.testingWorld.com'

#find the length of the string
print(len(stringEmail)) #20

#convert string into upper case
print(stringEmail.upper()) #WWW.TESTINGWORLD.COM

#convert string into lower case
print(stringEmail.lower()) #www.testingworld.com

#print the first letter of the string in capital
print(stringEmail.capitalize()) #Www.testingworld.com

stringIndiaEmail = '  www.testingworldindia.com   '

print(len(stringIndiaEmail)) #30



#remove leading spaces in the string
print(stringIndiaEmail.lstrip()) #www.testingworldindia.com

#remove trailing spaces 'end spaces'
print(stringIndiaEmail.rstrip()) #  www.testingworldindia.com

#remove leading and trailing spaces
print(stringIndiaEmail.strip()) #www.testingworldindia.com

email = 'xyz123@gmail.com'

#replace gmail with yahoo
print(email.replace("gmail", "yahoo"))

#find no. of 'm' in the string
#Way - 1
z = 0
for i in email:
    if(i=='m'):
        z = z+1
print(z)

#Way - 2
x = len(email)
y = len(email.replace("m", ""))
print("no. of m's in the straing = " + str(x-y))

email1 = "gmail"

#find function - is used to find string in another string

print(email.find(email1)) #output = 7, because on the 7th index of email gmail starts

emailAddress = 'this is my email id mybike3412@gmail.com'

#split function - is used to remove spaces
list1 = emailAddress.split(" ")
print(len(list1)) #6

print(list1) # ['this','is','my','email','id','mybike3412@gmail.com']
