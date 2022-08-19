#Write a Python program to generate and print a list of first and last 5 elements where 
#the values are square of numbers between 1 and 30 (both included).

def list(number):
    i=1
    square=0
    a=[]
    b=[]
    while i<=number:
        square=i**2
        a.append(square)
        i=i+1
    x=(a[:5])
    y=(a[25:])
    b.append(x)
    b.append(y)
    print(b)
list(30)


#Write a Python function to create and print a list where the values are square of numbers
#between 1 and 30 (both included). 
# def square(number):
#     i=1
#     list=[]
#     while i<=number:
#         list.append(i**2)
#         i=i+1
#     print(list)
# square(30)