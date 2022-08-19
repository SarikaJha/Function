#Define a function which takes one parameter(positive integer). This function 
#returns the sum of all multiples of 3 and 5 (not neccessary common multiples) 
#in the range 1 to the integer passed as the parameter.
def multiples(num):
    i=1
    sum=0
    while i<=num:
        if i%3==0 or i%5==0:
            sum=sum+i
        i=i+1
    print(sum)
num=int(input("enter the number:"))
multiples(num)
