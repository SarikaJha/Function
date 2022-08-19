def remainder(a,b):
    c=0
    if a>b:
        c=a%b
    elif a<b:
        c=b%a
    print(c)
a=int(input("enter the number:"))
b=int(input("enter the number:"))
remainder(a,b)