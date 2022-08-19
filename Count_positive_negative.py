#Given a list of numbers, write a Python program to count positive and negative numbers in a 
#List using function.

def positive_negative(list):
    positive_count=0
    negative_count=0
    i=0
    while i<len(list):
        if list[i]>0:
            positive_count+=1
        else:
            negative_count+=1
        i=i+1
    print("Number of positive:", positive_count)
    print("Number of negative:", negative_count)
list=[2, -7, 5, -64, -14]
positive_negative(list)