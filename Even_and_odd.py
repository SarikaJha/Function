#Define a function which takes one argument which is the limit upto which the
#  function has to print the numbers and their label(even or odd).
def even_and_odd(limit):
    i=1
    while i<=limit:
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
        i=i+1
limit=int(input("enter the number:"))
even_and_odd(limit)
