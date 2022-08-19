def factorial(number):
    i=1
    fac=1
    while i<=number:
        fac=fac*i
        i=i+1
    print(fac)
number=int(input("enter the number:"))
factorial(number)