def prime(m,n):
    i=m
    while i<=n:
        j=2
        count=0
        while j<i:
            if i%j==0:
                count=count+1
            j=j+1
        if count==0:
            print(i,"prime" )
        i+=1
m=int(input("enter the number:"))
n=int(input("enter the number:"))
prime (m,n)

# def prime(n,m):
#     a=[]
#     i=n
#     while i<=m:
#         if i%2!=0 or i==2:
#             a.append(i)
#         i=i+1
#     print(a)
# n=int(input("enter the number:"))
# m=int(input("enter the number:"))
# prime(n,m)