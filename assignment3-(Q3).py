#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#﻿Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12

#                                       ANSWER
a=input("Enter sample string : ")
def string(a):
    upper_value=0
    lower_value=0
    for i in a:
        if i.isupper():
            upper_value=upper_value+1
        elif i.islower():
            lower_value=lower_value+1
    print("Upper case letters is : ", upper_value)
    print("Lower case letters is : ", lower_value)
string(a)