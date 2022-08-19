#You have to print the largest value out of the given list using the max function.
#numbers = [3, 5, 7, 34, 2, 89, 2, 5]
# def function_name(numbers):
#     i=0
#     a=[]
#     while i<len(numbers):
#         a=max(numbers)
#         i+=1
#     print(a)
# numbers=[3,5,7,34,2,89,2,5]
# function_name(numbers) 


def maximum(numbers):
    i=0
    max=numbers[0]
    while i<len(numbers):
        if numbers[i]>max:
            max=numbers[i]
        i+=1
    print(max)
numbers=[121,3,5,100,34,2,89,2,5]
maximum(numbers)