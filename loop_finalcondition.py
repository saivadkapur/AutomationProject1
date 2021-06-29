#FOR LOOP WITH FINAL RANGE

#in  python number always start with zero and the value mentioned in the range is excluded from execution
#in below for loop condition the output will be 0,1,2.....,9
#for i in range(3):
    #print(i)

number = input("enter the number")
n = int (number)
#for i in range(n):
    #print(i)

#FOR LOOP WITH STARTING AND FINAL VALUE
#print table for the entered number output should be in number * 1 = Number

for i in range(1,4):
    print(str(n) + ' * ' + str(i) +' = '+ str (n*i))

#FOR LOOP WITH INCREMENT VALUE
#In the below line of code 1 is the starting point, 11 is the ending point and 2 is the increment value
#each time the loop is executed
for i in range(1,11,2):
    print(i) #1,3,5,7,9

#FOR LOOP WITH DECREMENT VALUE
for i in range(10,1,-2):
    print(i) #10,8,6,4,2

#FOR LOOP WITH LIST
list1 = [1,3,6,'test','automation']
for i in list1:
    print(i)#1,3,6,test,automation

for i in 'hello':
    print(i)#h,e,l,l,o

#FOR LOOP WITH ELSE STATEMENT
for i in range(1,4):
    print(i)
else:
    print('the loop is ended')
#Output- 1,2,3,the loop is ended