def upper_lower(a):
    i=0
    upper=0
    lower=0
    while i<len(a):
        if a[i].isupper():
            upper+=1
        else:
            lower+=1
        i+=1
    print("UPPERcase:",upper)
    print("lowercase:",lower)
upper_lower("IamNavgurukulStudentInBangalore")