#Use the min function and find the minimun value of the list.
#list = [8, 6, 4, 8, 4, 50, 2, 7]
# def minimum(numbers):
#     i=0
#     a=[]
#     while i<len(numbers):
#         a=min(numbers)
#         i=i+1
#     print(a)
# numbers=[8,6,4,8,4,50,2,7]
# minimum(numbers)

def minimum(numbers):
    i=0
    min=numbers[0]
    while i<len(numbers):
        if numbers[i]<min:
            min=numbers[i]
        i+=1
    print(min)
numbers=[121,3,5,100,34,89,2,5]
minimum(numbers)