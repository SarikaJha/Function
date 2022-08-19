# a=[4,3,2,8]
def multiple_max(a):
    i=0
    b=[]
    while i<len(a)-1:
        c=int(a[i])*int(a[i+1])
        b.append(c)
        i=i+1
    print(b)
    j=0
    max=0
    while j<len(b):
        if b[j]>max:
            max=b[j]
        j=j+1
    print(max)
a=input("enter: ")
multiple_max(a)