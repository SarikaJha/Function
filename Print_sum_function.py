#You have to print the sum of the elements of the given list by using the sum function.
#numbers = [1, 2, 3, 4, 5]
def total(numbers):
    i=0
    sum=0
    while i<len(numbers):
        sum=sum+numbers[i]
        i=i+1
    print("sum =",sum)
numbers=[1,2,3,4,5]
total(numbers)
