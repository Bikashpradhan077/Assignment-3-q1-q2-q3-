#Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20

#                                          ANSWER
Sample_List=(8,2,3,0,7)
def sum(Sample_List):
    sum1=0
    for i in Sample_List:
        sum1=sum1+i
    return sum1
print("Sum Of Numbers Are : " , sum(Sample_List))