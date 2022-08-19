def pair(list):
    i=0
    a=[]
    while i<len(list)-1:
        j=0
        while j<len(list):
            b=str(list[i])+str(list[j])
            a.append(b)
            j+=1
        i+=1
    print(a)
list=[4,3,2,8]
pair(list)
