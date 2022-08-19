def strong_password(password):
    digit='0123456789'
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower='abcdefghijklmnopqrstuvwxyz'
    special='!@#%$*...'
    sum=0
    a=0
    b=0
    c=0
    d=0
    if len(password)>6 or len(password)<=10:
        i=0
        while i<len(password):
            if password[i] in digit:
                a=1
            elif password[i] in upper:
                b=1
            elif password[i] in lower:
                c=1
            elif password[i] in special:
                d=1
            i+=1
        sum=a+b+c+d
        if sum<4:
            print("weak password")
        else:
            print("strong password")
password=input("enter the password:")
strong_password(password)