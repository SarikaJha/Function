def phone_no():
    a=([1,2,3,0,5,6,0,8,9])
    b=""
    c=""
    d="-"
    i=0
    while i<len(a):
        if i<3:
            b=b+str(a[i])
        elif i>=3 and i<=5:
            c=c+str(a[i])
        elif i>5 and i>=6:
            d=d+str(a[i])
        i=i+1
    y="("+b+")"
    print("phone no:",y+c+d)
phone_no()