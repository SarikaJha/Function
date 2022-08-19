#First of all take one parameter that is number from user and return table of the number by using recursion.
# def table(number):
#     i=1
#     while i<=10:
#         print(number,"*",i,"=",number*i)
#         i=i+1
# number=int(input("enter the number:"))
# table(number)

def table(number, i):
    print(number,"*",i,"=",number * i)
    if i<10:
        table(number, i + 1)
i=int(input("enter initialization:"))
number=int(input("enter number:"))
table(number, i)
