#Dictionary is used to store the values in key, value pair
#placed inside {}
#key must always be unique
#key and value could be any datatype
#value can be fetch by passing key

dic1 = {"k1":"val1", 2:"val2", "k3":3, "k1":"val4"}
print(dic1) #{'k1': 'val4', 2: 'val2', 'k3': 3} because keys should be unquie and last value will be assigned to duplicate keys

#updating the value
dic1[2] = "val3" #pass the key value for which you want to update the value
print(dic1) #{'k1': 'val4', 2: 'val3', 'k3': 3}

print(dic1["k3"]) #3

#add new key and its value
dic1["k4"] = 7
print(dic1) #{'k1': 'val4', 2: 'val3', 'k3': 3, 'k4': 7}

#Additional Method in Dictionary

#Keys method - used to fetch all the keys of the dictionary
print(dic1.keys()) # dict_keys(['k1', 2, 'k3', 'k4'])

#Values method - used to fetch all the values of the dictionary
print(dic1.values()) # dict_values(['val4', 'val3', 3, 7])

#items method - used to fetch both keys and values of dictionary
print(dic1.items()) # dict_items([('k1', 'val4'), (2, 'val3'), ('k3', 3), ('k4', 7)])

#find the length of dictionary
print(len(dic1)) #4



