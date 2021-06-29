#Tuple is similar to list we store similar or different datatypes
#all the data is placed in () but in list data is placed in[] in both the datatypes values are separated by comma
#in Tuple we cannot update/change any value and also we canot increase or decrease the Tuple size
#fetch element of tuple is the same way we do it in the list
#fetch length of the tuple is the same way we do it in the list

tuple1 = (1, 7, 'this', 9, 'ok', 12.56, 'ok', 7, 3)

print(len(tuple1)) #9
print(tuple1[2]) #this

#Advanvced Tuple Operations

#Count Method
#print no. of time string 'ok' is repeated in the tuple1
print(tuple1.count('ok')) #2

#find the index of an element in the tuple
print(tuple1.index(12.56)) #5

#Merge or Join two Tuples
tuple2 = (100, 200)
tuple3 = tuple1 + tuple2
print(tuple3) #(1, 7, 'this', 9, 'ok', 12.56, 'ok', 7, 3, 100, 200)

#display all the values in tuple
for i in tuple3:
    print(i)

