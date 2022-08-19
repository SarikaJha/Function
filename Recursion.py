# def odd_even(num):
#     x=str(num)
#     i=0
#     sum=0
#     while i<len(x):
#         sum=sum+int(x[i])
#         i+=1
#     s=str(sum)
#     if len(s)==1:
#         if int(s)%2==0:
#             print(s,"even")
#         else:
#             print(s,"odd")
#     else:
#         num=s
#         return(odd_even(sum))
# num=int(input("enter the number:"))
# odd_even(num)

def even(n):
    if n>9:
        i=0
        sum=0
        re=0
        while i<n:
            re=n%10
            sum=sum+re
            n=n//10
        return even(sum)
    else:
        if n%2==0:
            print(n,"even")
        else:
            print(n,"odd")
n=int(input("enter the number:"))
even(n)