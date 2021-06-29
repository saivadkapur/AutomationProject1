#LIST is used to store the data of similar or different datatypes
#List functions

list1 = [12,34.67,'testing',5,'is']

#fetch using index
print(list1[2]) #testing

#fetch using start and end index
print(list1[1:2]) #[34.67]

#fetch using starting index
print(list1[3:]) #[5, 'is']

#fetch using end index
print(list1[:3]) #[12, 34.67, 'testing']

#update list
list1[3] = 'abc' #replace the 3rd index value with 'abc'
print(list1) #[12, 34.67, 'testing', 'abc', 'is']

#add to list
list1.insert(2,12)
print(list1) #[12, 34.67, 12, 'testing', 'abc', 'is']

#remove from the list
list1.remove(12) #though there are 2 no. of '12' present in the list but only the first occurance is removed
print(list1) #[34.67, 12, 'testing', 'abc', 'is']

#find the length of the list using len
print(len(list1)) #5

#CMP function is used to compare two lists
#cmp(list1,list2) this feature is not supported for python 3 0r greater versions

#list concetination
list2 = [1, 7, 'xyz']
print(list1 + list2) #[34.67, 12, 'testing', 'abc', 'is', 1, 7, 'xyz']



