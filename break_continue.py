#BREAK - when the condition is true and reaches break statement then the compiler will exit the loop

number = input('enter the number--> ')
for i in range(1,11):
    if(int(number)*i == 60):
        break
    print(int(number)*i) #number = 12; output = 12,24,36,48

#CONTINUE - when the condition is true and reaches continue at the point the compiler will skip the below code
#repeate the loop until the condition is false
n = input('enter the number--> ')
for i in range(1,21):
    if((int(n)*i)%10 ==0):
        continue
    print(int(n)*i) #number = 6; Output = 6,12,18,24,36,42,48,54
