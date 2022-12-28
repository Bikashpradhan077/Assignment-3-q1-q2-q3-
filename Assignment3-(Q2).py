#Write a Python program to reverse a string.
#﻿Sample String : "1234abcd"
#Expected Output : "dcba4321"

#                                      ANSWER
def reverse_string(x):
    return x[::-1]
string=str(input("Enter a sample string: "))
string=reverse_string(string)
print("Reversed string is : ", string)