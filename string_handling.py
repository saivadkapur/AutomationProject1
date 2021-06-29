#strind can be stored in ' ', " ", & """ """
#if the string has already included ' ' then we use " " for the entire string and viseversa
#example

textbook = "the 'legendary' of the era"
print(textbook) #Output: the 'legendary' of the era

textbook = 'the "drama" queen'
print(textbook) #Output: the "drama" queen

#if your string is in multiple line then we use """ """
companydetails = """
name: abc
url: www.abc.com
email: inquire@abc.com
phone: 12345
"""
print(companydetails)

# '+' operator is used for string concetanation
# '*' operator is used to display the same string for multiple times

#print(companydetails * 3) #Output - company details are displayed for 3 times


stringName = "www.learnpython.com"

#fetch the string using any index
print(stringName[6]) #a

#fetch substring my giving start and end index
print(stringName[3:8]) #.lear

#fetch string my giving starting index
print(stringName[6:]) #arnpython.com

#fetch string my giving end index
print(stringName[:7]) #www.lea


