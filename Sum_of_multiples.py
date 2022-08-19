# def multiples(a,b):
#     i=0
#     sum=0
#     while i<=b:
#         if i%a==0:
#             sum=sum+i
#     print (sum)
# a=int(input("enter the number:"))
# b=int(input("enter the second number:"))
# multiples(a,b)


def multiples(a,b):
    if b<0 or a<0:
        print("invalid")
    else:
        i=a
        sum=0
        while i<=b:
            if i%a==0:
                sum=sum+i
            i+=1
        print (sum)
a=int(input("enter the number:"))
b=int(input("enter the second number:"))
multiples(a,b)

# def multiples(a,b):
#     if b>0 and a>0:
#         i=0
#         sum=0
#         while i<=b:
#             if i%a==0:
#                 sum=sum+i
#             i+=1
#         print (sum)
#     else:
#         print("invalid")
# a=int(input("enter the number:"))
# b=int(input("enter the second number:"))
# multiples(a,b)