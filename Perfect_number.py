#Define a function named perfect() which takes one argument(integer) and checks if it is a perfect 
#number or not. Now use this code to write a program that prints all the perfect numbers between 1-1000.
#"part 1"
# def perfect():
#     num=int(input("enter the number:"))
#     i=1
#     sum=0
#     while i<num:
#         if num%i==0:
#             sum=sum+i
#         i=i+1
#     if sum==num:
#         print("perfect number")
#     else:
#         print("not perfect number")
# perfect()

#"part 2"
def perfect(n):
    i=1
    while i<=n:
        j=1
        sum=0
        while j<i:
            if i%j==0:
                sum=sum+j
            j+=1
        if sum==i:
            print(i)
        i+=1
perfect(1000) 