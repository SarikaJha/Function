# n1=int(input("enter the number:"))
# n2=int(input("enter the number:"))
# def add():
#     add=n1+n2
#     return add
# def sub():
#     sub=n1-n2
#     return sub
# def mul():
#     mul=n1*n2
#     return mul
# def div():
#     div=n1/n2
#     return div
# def main_func():
#     n=input("enter the number:")
#     if n=="add":
#         print(add())
#     elif n=="sub":
#         print(sub())
#     elif n=="mul":
#         print(mul())
#     elif n=="div":
#         print(div())
# main_func()

#SIMPLE CALCULATOR
a=int(input("enter the number:"))
b=int(input("enter the number:"))
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x//y
print("select operator")
while True:
    choice=input("enter choice(1/2/3/4)")
    if choice=="1":
        print(a,"+",b,"=",add(a,b))
    elif choice=="2":
        print(a,"-",b,"=",sub(a,b))
    elif choice=="3":
        print(a,"*",b,"=",mul(a,b))
    elif choice=="4":
        print(a,"/",b,"=",div(a,b))
    break