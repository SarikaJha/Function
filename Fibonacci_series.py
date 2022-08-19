# def fibonacci(num):
#     a,b=0,1
#     i=1
#     while i<num:
#         print(a)
#         i=i+1
#         a,b=b,a+b
# num=int(input("enter the number:"))
# fibonacci(num)

x=300
def my_function():
    global x
    x=200
my_function()
print(x)