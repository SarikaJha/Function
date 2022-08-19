#Create a function which takes one argument (a positive integer) and returns a
#dictionary which has numbers from 1 to the integer (passed as parameter) as the
#keys and their respective squares as the values.
def squares(number):
    i=1
    while i<=number:
        print(i,":",i**2,end=", ")
        i=i+1
number=int(input("enter the number:"))
squares(number)
print()